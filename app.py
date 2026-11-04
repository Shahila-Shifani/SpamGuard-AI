import streamlit as st
from predict import load_model, predict_message

st.set_page_config(page_title="SpamGuard-AI", page_icon="✉️")
st.title("SpamGuard-AI")
st.write("A beginner machine learning project that classifies an SMS message as spam or not spam.")
st.caption("Predictions are estimates from a model trained on a public SMS dataset.")
try:
    model, vectorizer = load_model()
    message = st.text_area("Enter an SMS message", height=140, placeholder="Congratulations! You have won...")
    if st.button("Predict", type="primary"):
        if not message.strip():
            st.warning("Please enter a message.")
        else:
            label = predict_message(message, model, vectorizer)
            if label == "spam":
                st.error("Prediction: Spam")
            else:
                st.success("Prediction: Not spam")
            st.write("The model uses word-frequency features (TF-IDF) and Multinomial Naive Bayes.")
except FileNotFoundError:
    st.warning("The trained model is not available yet. Download the dataset and run `python train_model.py` first.")
except Exception as error:
    st.error(f"Could not load the model: {error}")
