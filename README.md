# Liver Disease Prediction

# Overview
This project develops a machine learning model to predict liver disease using clinical data. By applying supervised learning techniques and in-depth exploratory data analysis, it provides insights into the key contributing factors and achieves accurate predictions. A Flask-based web portal is also integrated for user interaction and visualization.

# Problem Statement
Liver diseases are a significant global health concern, contributing to substantial morbidity and mortality. Traditional diagnostic methods are often invasive and inaccessible to many individuals. This project aims to create a predictive model leveraging clinical features to enable early detection and intervention.

# Dataset
The dataset used is the Indian Liver Patient Dataset, containing 583 patient records and the following features:

Age

Gender

Total Bilirubin, Direct Bilirubin

Alkaline Phosphatase, Alanine Aminotransferase, Aspartate Aminotransferase

Total Proteins, Albumin, Albumin and Globulin Ratio

Target: Indicates the presence (1) or absence (0) of liver disease.

# Key Features

# Domain Analysis
Age: Older individuals are at higher risk.

Gender: Males generally face higher risk due to lifestyle factors.

Total Bilirubin: Elevated levels indicate liver dysfunction.

Direct Bilirubin: Important for understanding bile duct issues.

Alkaline Phosphatase (ALP): High levels suggest liver or bile duct obstruction.

Alanine Aminotransferase (ALT) and Aspartate Aminotransferase (AST): Elevated levels signal liver damage.

Total Proteins: Low levels indicate liver disease or nutritional issues.

Albumin: Indicates chronic liver damage.

Albumin and Globulin Ratio: Reflects liver function and immune system activity.

# Exploratory Data Analysis (EDA)
Univariate Analysis
Histograms and box plots were used to analyze distributions and detect skewness/outliers for features like Age, Total Bilirubin, and Albumin.

Bivariate Analysis
Violin plots, scatter plots, and box plots reveal relationships between features and the target variable. For example, Total Bilirubin levels are higher among patients with liver disease.

Multivariate Analysis
Pairplot analysis uncovers correlations between features, such as strong relationships between Total Bilirubin and Direct Bilirubin.

# Data Preprocessing
Steps Taken
Handling Missing Values: Imputed missing values in Albumin and Globulin Ratio using the median.

Outlier Detection and Handling: Applied the IQR technique to reduce the impact of extreme values.

Encoding:

Gender: Female → 0, Male → 1.

Target: 1 → Disease, 0 → No Disease.

Feature Selection: Dropped Gender and Total Proteins due to low correlation with the target variable.

SMOTE: Balanced the dataset to address class imbalance.

Scaling: Standardized feature values for better model performance.

# Machine Learning Models
# Models Implemented
Logistic Regression

Decision Tree Classifier

Random Forest Classifier

Bagging Classifier

Gradient Boosting Classifier

XGBoost Classifier

Support Vector Machine (SVM)

Naive Bayes

K-Nearest Neighbors (KNN)

# Performance Metrics
F1 Score: Balances precision and recall.

Cross-Validation Score: Ensures model robustness.

ROC AUC: Measures the ability to distinguish between positive and negative classes.

# Results
Model	F1 Score	Cross-Validation Score	ROC AUC Score
Logistic Regression	0.68	0.67	0.77
Decision Tree Classifier	0.74	0.69	0.75
# Random Forest Classifier	0.82	0.75	0.93
Bagging Classifier	0.77	0.72	0.89
Gradient Boosting Classifier	0.79	0.77	0.90
XGBoost Classifier	0.82	0.77	0.90
Support Vector Machine	0.67	0.66	0.75
Naive Bayes	0.62	0.68	0.50
K-Nearest Neighbors	0.77	0.67	0.80
Insight: The Random Forest Classifier demonstrated the best performance, with high F1 and ROC AUC scores.

# Web Portal
# Overview
A Flask-based web portal is integrated for user interaction with the liver disease prediction model.

# Features
Interactive Interface: Users can input clinical data and receive real-time predictions.

Visualizations: Dynamic plots (histograms, violin plots) provide insights into the dataset.

Accessibility: Designed for local use, with potential for future deployment.

# How to Run the Web Portal

# Clone the repository:
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
# Install dependencies:
pip install -r requirements.txt
# Run the flask application
python app.py
# Access the portal at:
http://127.0.0.1:5000/

# Challenges Faced
Handling Outliers: Used IQR but couldn't address all due to high variability.

Model Overfitting: Random Forest showed overfitting despite hyperparameter tuning; it remained the best model.

Class Imbalance: Balanced using SMOTE to ensure robust predictions.

# Conclusion
The ensemble methods, especially Random Forest and XGBoost, proved most effective in predicting liver disease, achieving high diagnostic accuracy and reliability. The integrated web portal enhances usability by providing interactive predictions and visual insights.
