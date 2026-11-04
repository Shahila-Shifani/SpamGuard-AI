# Beginner guide

- **Dataset:** a table of examples. Here each SMS has a label and message.
- **Preprocessing:** small text cleanups before modelling.
- **TF-IDF:** turns text into numbers. Words common in one message but less common across all messages can receive higher weight.
- **Training data:** examples used to learn model patterns.
- **Testing data:** held-out examples used to estimate performance on unseen data.
- **Multinomial Naive Bayes:** a probability-based classifier that often works well with word-count-like features.
- **Confusion matrix:** a table showing true and predicted classes. This project prints it with `ham` first and `spam` second.

`train_model.py` performs the workflow. `predict.py` loads the saved model and vectorizer. The vectorizer must be saved too, because new messages must be converted using the same vocabulary and weighting learned during training.
