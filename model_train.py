# model_train.py
import pandas as pd
from feature_extractor import extract_features
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

print("Loading dataset...")
try:
    df = pd.read_csv('dataset.csv')
except FileNotFoundError:
    print("Error: dataset.csv not found.")
    print("Please create a dataset.csv file with 'url' and 'label' columns.")
    exit()

print("Extracting features from URLs... This may take a moment.")
features_list = df['url'].apply(extract_features).tolist()
X = pd.DataFrame(features_list)
y = df['label']

print(f"Feature extraction complete. Shape of feature matrix: {X.shape}")
print("Features used:", ", ".join(X.columns))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("Training the RandomForest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
print("Model training complete.")

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.4f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Safe', 'Fraud']))
print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\nSaving model to 'phishing_model.pkl' and features to 'model_features.joblib'")
joblib.dump(model, 'phishing_model.pkl')
joblib.dump(X.columns.tolist(), 'model_features.joblib')

print("Process finished.")

