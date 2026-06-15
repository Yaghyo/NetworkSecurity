# 🛡️ Phishing Domain Detection System: End-to-End MLOps Pipeline

## 📖 Comprehensive Overview
The Phishing Domain Detection System is a robust, production-ready machine learning pipeline engineered to identify malicious URLs and phishing domains based on granular network data. Rather than just building a model in a notebook, this project emphasizes **MLOps principles**, ensuring the model is scalable, maintainable, and continuously deployable. 

It covers the entire data lifecycle: from automated ingestion of complex URL attributes via a NoSQL database (MongoDB) to a fully containerized web application deployed through an automated CI/CD pipeline.

## 📊 Dataset Overview (`phisingData.csv`)
The project utilizes a highly structured dataset containing categorical features extracted from web page characteristics and URLs. The features are primarily encoded as `-1` (Phishing/Suspicious), `0` (Suspicious), and `1` (Legitimate).

### **Target Variable:**
* `Result`: The final classification predicting whether a domain is legitimate or a phishing attempt.

### **Key Feature Categories (30 Predictors):**
* **Address Bar Features:** Attributes directly extracted from the URL structure. 
  * *Examples:* `having_IP_Address`, `URL_Length`, `having_At_Symbol`, `Prefix_Suffix`, `having_Sub_Domain`, `double_slash_redirecting`.
* **Abnormal/Network Features:** Indicators of suspicious routing or abnormal requests.
  * *Examples:* `Request_URL`, `URL_of_Anchor`, `Links_in_tags`, `SFH` (Server Form Handler), `Submitting_to_email`, `Abnormal_URL`.
* **HTML and JavaScript Features:** Behavioral traits embedded within the page code.
  * *Examples:* `on_mouseover` (status bar obfuscation), `RightClick` (disabling right-click), `popUpWidnow`, `Iframe`, `Redirect`.
* **Domain & Security Attributes:** Trust indicators and third-party metrics.
  * *Examples:* `SSLfinal_State` (HTTPS validity), `Domain_registeration_length`, `age_of_domain`, `web_traffic`, `Page_Rank`, `Google_Index`.

## 🏗️ Architectural Deep Dive
The system is built using a highly modular architecture, separated into distinct pipeline components:

1. **Data Ingestion (`DataIngestion`):** Connects to MongoDB clusters to fetch the real-time `phisingData` network records. It splits the raw data into training and testing sets, storing them in the `artifacts/` directory for reproducibility.
2. **Data Validation (`DataValidation`):** Validates the incoming dataset against a strictly defined schema (`data_schema/`) mapping all 30 features. It detects data drift and ensures no missing or unexpectedly formatted variables break the pipeline.
3. **Data Transformation (`DataTransformation`):** Handles missing values via imputation and applies necessary encoding. Since the dataset is heavily categorical (-1, 0, 1), the transformer ensures the data shape is preserved and optimized. The transformation object is saved as a pickle file (`preprocessor.pkl`).
4. **Model Training (`ModelTrainer`):** Evaluates multiple classification algorithms suitable for categorical/boolean features (such as Random Forest, Decision Trees, or Gradient Boosting). It performs hyperparameter tuning, selects the best-performing model based on accuracy and F1-score (critical for phishing detection to minimize false negatives), and serializes the final model (`model.pkl`).
5. **Prediction Pipeline:** A dedicated module to handle single or batch predictions from the web interface, seamlessly routing user inputs (URL metrics) through the preprocessor and into the active model.

## 🚀 DevOps & CI/CD Workflow
* **Containerization:** The entire application, including the Flask/FastAPI server and serialized model artifacts, is packaged into a Docker image via the `Dockerfile`.
* **GitHub Actions:** The `.github/workflows/` directory contains YAML configurations that trigger on every push to the `main` branch. The pipeline automatically:
  1. Lints and tests the Python code.
  2. Builds a new Docker image.
  3. Pushes the image to a container registry (e.g., Docker Hub or AWS ECR).
  4. Triggers the deployment environment to pull the latest image.

## 🛠️ Detailed Tech Stack
* **Core:** Python 3.8+
* **ML Libraries:** Scikit-Learn, Pandas, NumPy, SciPy
* **Database:** MongoDB (Atlas/Local)
* **Web Interface:** Flask/FastAPI, HTML/CSS
* **Infrastructure:** Docker, GitHub Actions, AWS/Heroku (Deployment targets)