# Liver_Disease_Prediction
Liver Disease Prediction — Machine Learning Project
This project focuses on building and evaluating multiple machine learning models to predict liver disease using clinical data. It includes thorough data preprocessing, exploratory analysis, model comparison, and performance evaluation using metrics like F1-score, ROC AUC, and cross-validation. A lightweight Flask-based web portal is also included for user-friendly prediction access.

# Problem Statement
Develop a predictive model to identify individuals at high risk of liver disease based on clinical features, enabling early intervention and preventive care.

# Dataset Overview
Source: Indian Liver Patient Dataset (ILPD)

Records: 583 patient entries

Features:

Age, Gender

Total & Direct Bilirubin

Alkaline Phosphatase, ALT, AST

Total Proteins, Albumin

Albumin and Globulin Ratio

Target (1 = Disease, 2 = No Disease → encoded to 1/0)

# Exploratory Data Analysis
Univariate, bivariate, and multivariate visualizations using Plotly, Seaborn, and Matplotlib

Feature insights:

ALT, AST, and Bilirubin levels show strong correlation with liver disease

Gender imbalance noted (more male patients)

Outliers handled using IQR method

# Data Preprocessing
Missing value imputation (median for skewed features)

Label encoding for categorical variables

Feature scaling using StandardScaler

SMOTE applied to balance target classes

# Models Implemented
Model	F1 Score	ROC AUC	Cross-Validation
Logistic Regression	0.71	0.78	0.66
Decision Tree	0.65	0.69	0.69
Random Forest	0.83	0.93	0.75
Bagging Classifier	0.74	0.88	0.72
Gradient Boosting	0.80	0.92	0.74
XGBoost	0.85	0.94	0.74
SVM	0.68	0.75	0.63
Naive Bayes	0.62	0.50	0.68
K-Nearest Neighbors	0.71	0.79	0.68
# Best Model: XGBoost — selected for deployment based on highest F1 and ROC AUC scores.

# Feature Importance (XGBoost)
Feature	Importance
Alkaline Phosphatase	0.168
AST	0.145
ALT	0.126
Albumin & Globulin Ratio	0.123
Age	0.113
Total Bilirubin	0.113
Albumin	0.111
Direct Bilirubin	0.099
🌐 Web Portal (Flask)
A simple web interface allows users to input clinical parameters and receive predictions.

Frontend: HTML, Bootstrap, CSS

Backend: Flask

Model: Deployed using Pickle (model.pkl)

Result Display: Color-coded feedback (Green = No Disease, Red = Disease)

🚀 How to Run Locally
bash
# Clone the repo
git clone https://github.com/your-username/liver-disease-prediction

# Navigate to portal folder
cd portal

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
Visit http://127.0.0.1:5000 in your browser.


About Me
Ruchika Ambade MSc Statistics | Aspiring Data Scientist Skilled in predictive modeling, EDA, and dashboard design. Passionate about building impactful analytics solutions and exploring NLP & Generative AI. 📍 Based in Nagpur 
