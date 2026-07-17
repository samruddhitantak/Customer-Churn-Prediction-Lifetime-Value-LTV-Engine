import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Dataset
try:
    df = pd.read_csv("Customer Churn Prediction & Lifetime Value (LTV) Engine.csv")
except FileNotFoundError:
    print("Dataset file not found.")
    raise
print("\nDataset Shape:")
print(df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nFirst 5 Rows:")
print(df.head())

# 2. Data Cleaning
print("\nMissing Values:")
print(df.isnull().sum())

# Convert TotalCharges if present
if "TotalCharges" in df.columns: df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")

# Remove missing values
df.dropna(inplace=True)
print("\nDataset Shape After Cleaning:")
print(df.shape)
if len(df) == 0: raise ValueError("Dataset became empty after cleaning.")

# 3. Exploratory Data Analysis
if "Churn" in df.columns:
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x="Churn")
    plt.title("Customer Churn Count")
    plt.show()
if "Contract" in df.columns and "Churn" in df.columns:
    plt.figure(figsize=(8,5))
    sns.countplot(data=df, x="Contract", hue="Churn")
    plt.title("Contract Type vs Churn")
    plt.xticks(rotation=15)
    plt.show()

# 4. Feature Engineering
if "MonthlyCharges" in df.columns and "tenure" in df.columns:
    df["LTV"] = (df["MonthlyCharges"] *df["tenure"])
    print("\nLTV Column Created Successfully")
else:
    print("\nMonthlyCharges or tenure column not found")

# 5. Encode Categorical Columns
label_encoders = {}
for col in df.columns:
    if df[col].dtype == "object":
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le

# 6. Churn Prediction Model
if "customerID" in df.columns:
    df.drop("customerID", axis=1, inplace=True)
if "Churn" not in df.columns:
    raise ValueError("Churn column not found in dataset.")
X = df.drop("Churn", axis=1)
y = df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=42,stratify=y)
model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test,predictions)
print("\nModel Accuracy:")
print(f"{accuracy*100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test,predictions))

# Feature Importance
importance_df = pd.DataFrame({"Feature": X.columns,"Importance": model.feature_importances_})
importance_df = importance_df.sort_values(by="Importance",ascending=False)
print("\nTop 10 Features:")
print(importance_df.head(10))
plt.figure(figsize=(10,6))
sns.barplot(data=importance_df.head(10),x="Importance",y="Feature")
plt.title("Top 10 Important Features")
plt.show()

# 8. KPI Summary
print("Total Customers:", len(df))
if "MonthlyCharges" in df.columns:
    print("Average Monthly Charges:",round(df["MonthlyCharges"].mean(), 2))
if "tenure" in df.columns:
    print("Average Tenure:",round(df["tenure"].mean(), 2))
if "LTV" in df.columns:
    print("Average LTV:",round(df["LTV"].mean(), 2))
    
# 7. Customer LTV Segmentation
if "LTV" in df.columns:
    df["CustomerSegment"] = pd.cut(df["LTV"],bins=[0, 1000, 5000, np.inf],labels=["Low Value","Medium Value","High Value"])
    print("\nCustomer Segments:")
    print(df["CustomerSegment"].value_counts())
    plt.figure(figsize=(6,4))
    sns.countplot(data=df,x="CustomerSegment")
    plt.title("Customer Segments by LTV")
    plt.show()
print("Exit")
