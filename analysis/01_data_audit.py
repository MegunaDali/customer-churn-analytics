from pathlib import Path

import pandas as pd


# --------------------------------------------------
# Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "customer_churn.csv"


# --------------------------------------------------
# Load data
# --------------------------------------------------

df = pd.read_csv(DATA_PATH)


# --------------------------------------------------
# 1. Basic structure
# --------------------------------------------------

print("\n" + "=" * 60)
print("DATASET SHAPE")
print("=" * 60)

print(df.shape)


print("\n" + "=" * 60)
print("COLUMNS")
print("=" * 60)

for column in df.columns:
    print(column)


print("\n" + "=" * 60)
print("FIRST 5 ROWS")
print("=" * 60)

print(df.head())


# --------------------------------------------------
# 2. Data types
# --------------------------------------------------

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)


# --------------------------------------------------
# 3. Missing values
# --------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isna().sum())

print("\nTotal missing values:")
print(df.isna().sum().sum())


# --------------------------------------------------
# 4. Duplicate rows
# --------------------------------------------------

print("\n" + "=" * 60)
print("DUPLICATED ROWS")
print("=" * 60)

print(df.duplicated().sum())


# --------------------------------------------------
# 5. Descriptive statistics
# --------------------------------------------------

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

print(df.describe().T)


# --------------------------------------------------
# 6. Unique values
# --------------------------------------------------

print("\n" + "=" * 60)
print("UNIQUE VALUE COUNTS")
print("=" * 60)

for column in df.columns:
    print(f"{column}: {df[column].nunique()} unique values")


# --------------------------------------------------
# 7. Target distribution
# --------------------------------------------------

print("\n" + "=" * 60)
print("CHURN DISTRIBUTION")
print("=" * 60)

print(df["Churn"].value_counts())

print("\nChurn percentage:")
print(
    df["Churn"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)