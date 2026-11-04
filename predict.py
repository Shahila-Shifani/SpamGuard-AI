from pathlib import Path
import joblib
from text_preprocessing import clean_message

MODEL_DIR = Path("models")

def load_model():
    model_path = MODEL_DIR / "spam_model.joblib"
    vectorizer_path = MODEL_DIR / "tfidf_vectorizer.joblib"
    if not model_path.exists() or not vectorizer_path.exists():
        raise FileNotFoundError("Model files are missing. Run python train_model.py.")
    return joblib.load(model_path), joblib.load(vectorizer_path)

def predict_message(message, model=None, vectorizer=None):
    if model is None or vectorizer is None:
        model, vectorizer = load_model()
    cleaned = clean_message(message)
    features = vectorizer.transform([cleaned])
    return model.predict(features)[0]
