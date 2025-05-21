
import streamlit as st
import joblib

# Load trained model
model = joblib.load('Fake_news_detection.pkl')

st.title("📰 Fake News Detector")

user_input = st.text_area("Enter a news article text here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([user_input])[0]
        if prediction == 'fake':
            st.error("❌ This news appears to be Fake.")
        else:
            st.success("✅ This news appears to be Real.")
