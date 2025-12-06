# This script loads a messy sales dataset, cleans the data, and saves a cleaned CSV file.

import pandas as pd 

# Function to load a CSV file into a pandas DataFrame
# Changed file path from copilot suggestion to match the context provided/requirements 
def load_data(file_path: str): 
    df = pd.read_csv(file_path)
    return df

# Function to clean the column names
# It removes leading/trailing spaces, converts to lowercase, and replaces spaces with underscores
# Removed copilots additional cleaning steps for a more simplified and clear version that adheres to the requirements 
def clean_column_name(df):
    df.columns = (df.columns.str.strip().str.lower().str.replace(' ', '_'))
    if 'qty' in df.columns:
        df = df.rename(columns={'qty': 'quantity'})
    return df

# Handles missing values by filling them with appropriate default
# Price/quantity cannot be missing, so we remove rows where they are missing
def handle_missing_values(df):
    for col in ['price', 'quantity']:
        if col in df.columns: 
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna(subset=['price', 'quantity'])
    return df

# Removes invalid rows
# Negative prices or quantities are impossible and indicate data entry errors
def remove_invalid_rows(df):
    if 'price' in df.columns and 'quantity' in df.columns:
        df = df[(df['price'] >= 0) & (df['quantity'] >= 0)]
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_name(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())