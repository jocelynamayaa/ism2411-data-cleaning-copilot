# ISM2411 Data Cleaning with GitHub Copilot

This project is a small data-cleaning pipeline written in Python for my ISM2411 course. The goal of the assignment was to practice writing Python code, cleaning a messy CSV file, and using GitHub Copilot responsibly by reviewing and modifying its suggestions. 

The script loads a raw sales dataset, applies several cleaning steps, and then saves a clean CSV file in the 'processed' folder. 

# Project Structure

ism2411-data-cleaning-copilot/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv
│   └── processed/
│       └── sales_data_clean.csv        
├── src/
│   └── data_cleaning.py                
├── README.md                           
└── reflection.md                       

# What the Script Does

- Standardizes column names (lowercase with underscore)
- Removes extra spaces in text columns
- Handles missing prices/quantities 
- Removes rows with invalid values (negative prices or quantities)
- Saves the cleaned data to 'data/processed/sales_data_clean.csv'

# How to run

1. Make sure to have Python 3 installed and pandas if needed
2. From project root folder, run: python3 src/data_cleaning.py