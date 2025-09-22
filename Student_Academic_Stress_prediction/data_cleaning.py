# Data cleaning functions


import os
import pandas as pd
from config import RAW_DATA_PATH, CLEAN_DATA_PATH

def clean_data():
    # Load raw data
    df = pd.read_csv(RAW_DATA_PATH)

    # Example cleaning steps
    df = df.drop_duplicates()
    df = df.dropna()
    df.drop(columns=["Timestamp"], inplace=True, errors='ignore')

    # Save cleaned data: if file exists, replace it, else, create it
    if os.path.exists(CLEAN_DATA_PATH):
        os.remove(CLEAN_DATA_PATH)
    df.to_csv(CLEAN_DATA_PATH, index=False)
    print(f"✅ Cleaned data saved at {CLEAN_DATA_PATH}")

    return df.head()
    
if __name__ == "__main__":
    clean_data()
