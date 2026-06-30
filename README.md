# 📊 Customer Churn Prediction & Lifetime Value (LTV) Engine

## 🚀 Overview

The **Customer Churn Prediction & Lifetime Value (LTV) Engine** is a Data Science and Machine Learning project that predicts customer churn while estimating Customer Lifetime Value (LTV). The project combines data preprocessing, exploratory data analysis (EDA), feature engineering, machine learning, and business insights to help organizations identify customers who are likely to leave and determine their long-term value.

This project is built using Python and Scikit-learn, making it suitable for learning, portfolio building, and real-world business applications.

---

## 🎯 Objectives

- Predict whether a customer will churn.
- Calculate Customer Lifetime Value (LTV).
- Segment customers into different value groups.
- Identify key factors influencing churn.
- Generate business KPIs for decision-making.

---

## 🗂️ Dataset

The dataset contains customer information from a telecom company, including:

- Customer ID
- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract Type
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges
- Churn Status

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📁 Project Structure

```
Customer-Churn-LTV-Engine/
│
├── Customer.py
├── Customer Churn Prediction & Lifetime Value (LTV) Engine.csv
├── customer_churn_ltv_output.csv
├── README.md
├── requirements.txt
└── customer_churn_model.pkl
```

---

## ⚙️ Features

### Data Preprocessing

- Load dataset
- Handle missing values
- Convert data types
- Clean inconsistent data

### Exploratory Data Analysis (EDA)

- Churn distribution
- Contract vs Churn
- Customer insights
- Feature visualization

### Feature Engineering

Customer Lifetime Value (LTV)

```
LTV = Monthly Charges × Tenure
```

### Machine Learning

- Label Encoding
- Train-Test Split
- Random Forest Classifier
- Churn Prediction

### Model Evaluation

- Accuracy Score
- Precision
- Recall
- F1 Score
- Classification Report
- Feature Importance

### Customer Segmentation

Customers are classified into:

- Low Value
- Medium Value
- High Value

### KPI Dashboard

Displays:

- Total Customers
- Average Monthly Charges
- Average Tenure
- Average LTV

---

## 📊 Sample Output

### Model Accuracy

```
79.18%
```

### Top Important Features

- Monthly Charges
- Total Charges
- LTV
- Tenure
- Contract
- Tech Support
- Payment Method
- Online Security

### Customer Segments

```
Medium Value : 2992
Low Value    : 2897
High Value   : 1143
```

### KPI Summary

```
Total Customers : 7032
Average Monthly Charges : 64.80
Average Tenure : 32.42
Average LTV : 2283.15
```

---

## 📈 Visualizations

The project generates the following visualizations:

- Customer Churn Count
- Contract Type vs Churn
- Feature Importance
- Customer LTV Segmentation

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Customer-Churn-LTV-Engine.git
```

Move into the project folder

```bash
cd Customer-Churn-LTV-Engine
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python Customer.py
```

---

## 📋 Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
```

Install all packages

```bash
pip install -r requirements.txt
```

---

## 💼 Business Use Cases

- Telecom Customer Retention
- Banking Customer Analytics
- Subscription-Based Businesses
- E-commerce Customer Analysis
- SaaS Customer Success
- Marketing Campaign Optimization

---

## 📌 Key Insights

- Customers with month-to-month contracts are more likely to churn.
- Customers with longer tenure generally have higher lifetime value.
- Monthly charges significantly impact churn probability.
- Contract type is one of the strongest predictors of churn.
- High-value customers should be prioritized for retention strategies.

---

## 🔮 Future Enhancements

- Hyperparameter Tuning
- XGBoost and LightGBM Models
- Streamlit Web Dashboard
- Power BI Dashboard Integration
- SHAP Explainable AI
- Cross Validation
- ROC-AUC Curve
- Confusion Matrix Visualization
- Model Deployment using Flask/FastAPI
- Cloud Deployment (AWS/Azure)

---

## 👩‍💻 Author

**Samruddhi Tantak**

Data Analytics

---

## ⭐ If you found this project useful, consider giving it a star!