# SpamGuard-AI

## 1. About the project
SpamGuard-AI trains a text classifier to predict whether an SMS message is spam or ham (not spam).

## 2. Problem statement
Unwanted messages can contain scams or unwanted advertising. This project demonstrates a basic text-classification workflow.

## 3. Features
- Download the public SMS dataset.
- Inspect and clean messages.
- Convert text to TF-IDF features.
- Train a Multinomial Naive Bayes classifier.
- Print accuracy, precision, recall, F1-score and a confusion matrix.
- Save the trained model and predict a new message in Streamlit.

## 4. Technologies used
Python, pandas, scikit-learn, TF-IDF, Multinomial Naive Bayes, joblib and Streamlit.

## 5. Project folder structure
`train_model.py` trains and evaluates the model. `predict.py` loads it. `text_preprocessing.py` cleans text. `download_data.py` obtains the source dataset.

## 6. How to install
Python 3.10 or later is recommended.

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## 7. How to run
The dataset is downloaded from UCI on first training (internet required):
```bash
python train_model.py
streamlit run app.py
```

## 8. How it works
A dataset is a collection of examples. Each row has a label (`ham` or `spam`) and a message. Text preprocessing standardises text. TF-IDF converts words into numeric values that reflect how informative they are in the dataset. The data is split into training and test sets. Naive Bayes learns patterns from the training data and is evaluated on held-out messages.

A confusion matrix counts correct and incorrect predictions for each class. Accuracy is the overall fraction correct, but precision and recall matter because missing spam and incorrectly flagging a genuine message have different costs.

## 9. Screenshots
![Home Page](screenshots/SpamGuard-AI.png)

![Home Page](screenshots/SpamGuard-AI-b.png)

![Home Page](screenshots/SpamGuard-AI-c.png)

## 10. What I learned
Text cleaning, train/test splitting, TF-IDF, model training, evaluation metrics and saving a model.

## 11. Limitations
The dataset is historical and may not represent current scam messages, languages or regional patterns. Predictions can be wrong. Do not rely on it as a security filter.

## 12. Future improvements
Try other models, cross-validation, multilingual data and a larger up-to-date dataset.

## 13. Dataset/API credits
UCI Machine Learning Repository, **SMS Spam Collection**: https://archive.ics.uci.edu/dataset/228/sms+spam+collection. The downloader uses the UCI-hosted ZIP. Review the dataset page for citation and usage information.
