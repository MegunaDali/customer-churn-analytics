from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo


# --------------------------------------------------
# Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# Fetch dataset from UCI
# --------------------------------------------------

print("Fetching Iranian Churn dataset from UCI...")

iranian_churn = fetch_ucirepo(id=563)

X = iranian_churn.data.features
y = iranian_churn.data.targets


# --------------------------------------------------
# Combine features and target
# --------------------------------------------------

df = pd.concat([X, y], axis=1)


# --------------------------------------------------
# Basic verification
# --------------------------------------------------

print("\nDataset successfully fetched.")

print("\nFeatures shape:")
print(X.shape)

print("\nTarget shape:")
print(y.shape)

print("\nCombined dataset shape:")
print(df.shape)

print("\nColumns:")
for column in df.columns:
    print(f"- {column}")


# --------------------------------------------------
# Define output paths
# --------------------------------------------------

customer_csv_path = RAW_DATA_DIR / "customer_churn.csv"
customer_excel_path = RAW_DATA_DIR / "customer_churn.xlsx"

variables_csv_path = RAW_DATA_DIR / "variable_information.csv"
variables_excel_path = RAW_DATA_DIR / "variable_information.xlsx"


# --------------------------------------------------
# Save raw customer dataset
# --------------------------------------------------

df.to_csv(
    customer_csv_path,
    index=False
)

df.to_excel(
    customer_excel_path,
    index=False
)


# --------------------------------------------------
# Save UCI variable information
# --------------------------------------------------

variable_information = iranian_churn.variables

variable_information.to_csv(
    variables_csv_path,
    index=False
)

variable_information.to_excel(
    variables_excel_path,
    index=False
)


# --------------------------------------------------
# Confirmation
# --------------------------------------------------

print("\nFiles saved successfully:")

print(f"- {customer_csv_path}")
print(f"- {customer_excel_path}")
print(f"- {variables_csv_path}")
print(f"- {variables_excel_path}")