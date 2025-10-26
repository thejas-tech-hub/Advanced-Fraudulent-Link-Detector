# Advanced-Fraudulent-Link-Detector
ML-powered fraud and phishing link detection system | Python, scikit-learn, joblib
This project implements a machine learning-based system to detect potentially fraudulent or phishing links. It analyzes URLs based on various lexical and host-based features and uses a trained RandomForestClassifier model to classify them as "Safe" or "Fraud".

## ✨ Features

* **Feature Extraction**: Extracts numerous features from URLs including:
    * Length-based features (URL, hostname, path, first directory)
    * Count of special characters (`-`, `@`, `?`, `%`, `.`, `=`)
    * Presence of IP address in hostname
    * Use of URL shortening services
    * Counts of `http`, `https`, `www`
    * Digit and letter counts and ratios
    * Presence of sensitive keywords (e.g., 'login', 'bank', 'secure')
* **Machine Learning Model**: Utilizes a `RandomForestClassifier` trained on the extracted features to predict the likelihood of a URL being fraudulent.
* **Web Interface**: Provides a simple web interface using Streamlit to input a URL and view the prediction result and confidence score.

## 🛠️ Technology Stack

* **Python**: Core programming language.
* **scikit-learn**: For machine learning tasks (RandomForestClassifier, train_test_split, metrics).
* **pandas**: For data manipulation and handling the dataset.
* **joblib**: For saving and loading the trained model and feature list.
* **Streamlit**: For creating the interactive web application.
* **seaborn / matplotlib**: Used during model training for visualization (like confusion matrix, though not explicitly saved in the final app).

## ⚙️ How It Works

1.  **Feature Extraction**: The `feature_extractor.py` script takes a URL and extracts various characteristics based on its structure and content.
2.  **Model Training**: The `model_train.py` script loads a dataset (`dataset.csv` containing URLs and labels: 0 for safe, 1 for fraud), extracts features for each URL, splits the data, and trains a RandomForestClassifier model. The trained model (`phishing_model.pkl`) and the list of features used (`model_features.joblib`) are saved.
3.  **Prediction**: The `predictor.py` script (and `app.py`) loads the saved model and feature list. When a new URL is provided, it extracts its features, ensures they match the order expected by the model, and then uses the model to predict whether the URL is safe or fraudulent.
4.  **Web Interface**: `app.py` uses Streamlit to create a simple UI where users can paste a URL and get the prediction result in real-time.

## 🚀 Setup and Usage

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd advanced-fraudulent-link-detector
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure you have Python and pip installed.)*

3.  **Prepare Dataset:**
    * Make sure you have a `dataset.csv` file in the project directory. It should have at least two columns: `url` and `label` (0 for safe, 1 for fraudulent). A sample is included. For better performance, use a larger and more diverse dataset.

4.  **Train the Model:**
    ```bash
    python model_train.py
    ```
    * This will process the dataset, train the model, print evaluation metrics, and save `phishing_model.pkl` and `model_features.joblib`.

5.  **Run the Web Application:**
    ```bash
    streamlit run app.py
    ```
    * Open your web browser and navigate to the local URL provided by Streamlit.
    * Enter a URL in the input box and click "Analyze URL" to see the prediction.

## 📁 Project Files

* `app.py`: The Streamlit web application script.
* `model_train.py`: Script to train the RandomForest model using `dataset.csv` and save the model artifacts.
* `feature_extractor.py`: Contains the function to extract features from a given URL.
* `predictor.py`: Simple script demonstrating how to load the model and predict a single URL (used internally by `app.py`).
* `dataset.csv`: Sample dataset containing URLs and their labels.
* `requirements.txt`: Lists the necessary Python libraries.
* `phishing_model.pkl`: The saved, trained machine learning model file.
* `model_features.joblib`: A saved list containing the names of the features the model was trained on, in the correct order.
