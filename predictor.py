import joblib
from feature_extractor import extract_features

model = joblib.load('phishing_model.pkl')

def predict_url(url):
    features = extract_features(url)
    result = model.predict([features])[0]
    return "Fraud" if result else "Safe"
