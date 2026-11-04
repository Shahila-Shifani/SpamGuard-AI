from pathlib import Path
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from text_preprocessing import clean_message
from download_data import download_dataset

DATA_PATH = Path("data/SMSSpamCollection")
MODEL_DIR = Path("models")

def main():
    if not DATA_PATH.exists():
        download_dataset()
    data = pd.read_csv(DATA_PATH, sep="\t", header=None, names=["label", "message"], encoding="utf-8")
    data = data.dropna().drop_duplicates()
    data["clean_message"] = data["message"].apply(clean_message)
    X_train, X_test, y_train, y_test = train_test_split(
        data["clean_message"], data["label"], test_size=0.2, random_state=42, stratify=data["label"]
    )
    vectorizer = TfidfVectorizer()
    X_train_features = vectorizer.fit_transform(X_train)
    X_test_features = vectorizer.transform(X_test)
    model = MultinomialNB()
    model.fit(X_train_features, y_train)
    predictions = model.predict(X_test_features)
    print("Evaluation on held-out test data")
    print(f"Accuracy:  {accuracy_score(y_test, predictions):.3f}")
    print(f"Precision: {precision_score(y_test, predictions, pos_label='spam'):.3f}")
    print(f"Recall:    {recall_score(y_test, predictions, pos_label='spam'):.3f}")
    print(f"F1-score:  {f1_score(y_test, predictions, pos_label='spam'):.3f}")
    print("Confusion matrix (label order: ham, spam):")
    print(confusion_matrix(y_test, predictions, labels=["ham", "spam"]))
    print(classification_report(y_test, predictions))
    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_DIR / "spam_model.joblib")
    joblib.dump(vectorizer, MODEL_DIR / "tfidf_vectorizer.joblib")
    print("Saved model and vectorizer in models/")

if __name__ == "__main__":
    main()
