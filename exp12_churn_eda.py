"""Experiment 12: Exploratory Data Analysis (EDA) on customer churn data,
find patterns and clean the data  -- CO-4

If 'customer_churn.csv' exists it is used (it should have a 'Churn' column
with Yes/No). Otherwise a small sample dataset is generated automatically.
"""

import os
import numpy as np
import pandas as pd

FILE = "customer_churn.csv"


def make_sample_data(n=300):
    """Create a messy sample dataset (with missing values and duplicates)."""
    rng = np.random.default_rng(1)
    df = pd.DataFrame({
        "CustomerID": range(1, n + 1),
        "Gender": rng.choice(["Male", "Female"], n),
        "Tenure": rng.integers(1, 72, n),
        "Contract": rng.choice(["Month-to-month", "One year", "Two year"],
                               n, p=[0.55, 0.25, 0.20]),
        "MonthlyCharges": rng.normal(65, 25, n).round(2),
    })
    # Churn is more likely for month-to-month and short tenure
    prob = 0.1 + 0.4 * (df["Contract"] == "Month-to-month") \
               + 0.2 * (df["Tenure"] < 12)
    df["Churn"] = np.where(rng.random(n) < prob, "Yes", "No")
    # Add dirt
    df.loc[rng.choice(n, 15, replace=False), "MonthlyCharges"] = np.nan
    df.loc[rng.choice(n, 8, replace=False), "Gender"] = np.nan
    df = pd.concat([df, df.sample(5, random_state=1)])   # duplicates
    return df


# ------------------- 1. Load data -------------------
df = pd.read_csv(FILE) if os.path.exists(FILE) else make_sample_data()

print("=== 1. FIRST ROWS ===")
print(df.head())
print("\nShape:", df.shape)

# ------------------- 2. Understand data -------------------
print("\n=== 2. DATA TYPES & SUMMARY ===")
print(df.dtypes)
print(df.describe())

# ------------------- 3. Check problems -------------------
print("\n=== 3. MISSING VALUES ===")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# ------------------- 4. Clean data -------------------
df = df.drop_duplicates()                                  # remove duplicates
for col in df.select_dtypes(include="number").columns:     # numeric -> median
    df[col] = df[col].fillna(df[col].median())
for col in df.select_dtypes(include="object").columns:     # text -> mode
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove outliers in MonthlyCharges using the IQR rule
if "MonthlyCharges" in df.columns:
    q1, q3 = df["MonthlyCharges"].quantile([0.25, 0.75])
    iqr = q3 - q1
    df = df[df["MonthlyCharges"].between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)]

print("\n=== 4. AFTER CLEANING ===")
print("Shape:", df.shape, "| Missing values:", int(df.isnull().sum().sum()))

# ------------------- 5. Find patterns -------------------
print("\n=== 5. PATTERNS ===")
churn_rate = (df["Churn"] == "Yes").mean() * 100
print(f"Overall churn rate: {churn_rate:.1f}%")

for col in df.select_dtypes(include="object").columns:
    if col not in ("Churn", "CustomerID") and df[col].nunique() <= 10:
        rate = df.groupby(col)["Churn"].apply(lambda s: (s == "Yes").mean() * 100)
        print(f"\nChurn % by {col}:\n{rate.round(1)}")

print("\nAverage numeric values: churned vs not churned")
print(df.groupby("Churn").mean(numeric_only=True).round(2))

# Save the cleaned data
df.to_csv("churn_cleaned.csv", index=False)
print("\nCleaned data saved to churn_cleaned.csv")

# ------------------- 6. Optional chart -------------------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    df["Churn"].value_counts().plot(kind="bar", title="Churn Count")
    plt.savefig("churn_chart.png")
    print("Chart saved to churn_chart.png")
except ImportError:
    print("(matplotlib not installed, chart skipped)")
