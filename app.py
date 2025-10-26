# app.py
import streamlit as st
import joblib
import pandas as pd
from feature_extractor import extract_features

try:
    model = joblib.load('phishing_model.pkl')
    model_features = joblib.load('model_features.joblib')
except FileNotFoundError:
    st.error("Model files not found. Please run model_train.py first.")
    st.stop()

def predict_url(url):
    features_dict = extract_features(url)
    features_df = pd.DataFrame([features_dict])
    features_df = features_df[model_features]
    prediction = model.predict(features_df)[0]
    probability = model.predict_proba(features_df)[0]
    return prediction, probability

st.set_page_config(page_title="Fraud Link Detector", page_icon="🛡️", layout="wide")
st.title("🛡️ Advanced Fraudulent Link Detector")
st.markdown("This tool uses a machine learning model to analyze URLs and detect potential phishing or fraudulent links.")

url_input = st.text_input(
    "Enter a URL to analyze:", 
    placeholder="e.g., https://www.google.com"
)

if st.button("Analyze URL"):
    if url_input:
        with st.spinner('Analyzing...'):
            prediction, probability = predict_url(url_input)
            st.write("---")
            st.subheader("Analysis Result")
            if prediction == 1:
                st.error("⚠️ This link is likely **Fraudulent**.")
                st.warning(f"Confidence: {probability[1]:.2%}")
            else:
                st.success("✅ This link appears to be **Safe**.")
                st.info(f"Confidence: {probability[0]:.2%}")
    else:
        st.warning("Please enter a URL to analyze.")

st.sidebar.title("About")
st.sidebar.info(
    "This application uses a `RandomForestClassifier` to predict "
    "phishing URLs based on lexical and host-based features."
)
