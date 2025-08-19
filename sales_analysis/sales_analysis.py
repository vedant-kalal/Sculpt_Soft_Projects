import pandas as pd
import numpy as np


csv_file = input("Enter the path to the CSV file: ")
df = pd.read_csv(csv_file)

# DATA CLEANING

#1 Normalize Date to datetime

def normalize_date(df):
    try:
        df["Date"] = pd.to_datetime(df["Date"], format='mixed', errors='coerce')
        print("Date normalization complete.")
        return df
    except Exception as e:
        print(f"Error normalizing date: {e}")
        return None
    
#2 Fix/remove negative Units_Sold

def fix_negative_units_sold(df):
    df.loc[df['Units_Sold'] < 0, 'Units_Sold'] = df['Units_Sold']* -1
    print("Negative Units_Sold fixed.")
    return df

#3 Handle Revenue = 0 or negative

def handle_zero_negative_revenue(df):
    df.loc[df['Revenue'] <= 0, 'Revenue'] = df['Revenue']* -1
    df.loc[df["Revenue"] == 0.00, "Revenue"] = df["Revenue"].mean()
    print("Zero or negative Revenue handled.")
    return df

#4 Standardize Holiday to Yes/No

def standardize_holiday(df):
    df["Holiday"].replace({"Y": "Yes", "N": "No"}, inplace=True)
    df=df[df["Holiday"]!= "-"]
    print("Holiday column standardized to Yes/No.")
    return df

#5 Fill missing City using mode per store

def fill_missing_city(df):
    df['City'] = df.groupby('Store_ID')['City'].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 'Unknown'))
    print("Missing City values filled using mode per store.")
    return df


# adding columns for analysis
#1 Add Month

def add_month_column(df):
    df['Month'] = df['Date'].dt.month_name()
    print("Month column added.")
    return df

# add is_weekend column
def add_is_weekend_column(df):
    df['Is_Weekend'] = df['Date'].dt.day_name().isin(['Saturday', 'Sunday'])
    df["Is_Weekend"] = df["Is_Weekend"].replace({True: "Yes", False: "No"})
    print("Is_Weekend column added.")
    return df

# add avg selling price column
def add_avg_selling_price_column(df):
    df['Avg_Selling_Price'] = df['Revenue'] / df['Units_Sold']
    print("Avg_Selling_Price column added.")
    return df

def to_csv(df, output_file='cleaned_sales_data.csv'):
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")


# calling all functions
df = normalize_date(df)
df = fix_negative_units_sold(df)
df = handle_zero_negative_revenue(df)   
df = standardize_holiday(df)
df = fill_missing_city(df)
df = add_month_column(df)
df = add_is_weekend_column(df)
df = add_avg_selling_price_column(df)
to_csv(df)

# exploratory analysis
def exploratory_analysis(df):
    print("\nExploratory Analysis:")
    print("----------------------------")
    print(f"Monthly revenue:\n{pd.DataFrame(df.groupby("Month")["Revenue"].sum())}")
    print("----------------------------")
    print(f"Top 5 products by average price:\n{((pd.DataFrame(df.groupby("Product_ID")["Avg_Selling_Price"].sum()).replace(np.inf,np.nan)).dropna()).sort_values(by="Avg_Selling_Price", ascending=False).head()}")
    print("----------------------------")
    print(f"Weekend revenue by city:\n{pd.DataFrame(df[df['Is_Weekend'] == 'Yes'].groupby('City')['Revenue'].sum())}")
    print("----------------------------")
    print("correlation matrix:\n", df.drop(["Date","Store_ID","Product_ID","City","Holiday","Month","Is_Weekend"],axis=1).corr())
    print("----------------------------")


exploratory_analysis(df)
print("Data cleaning and analysis complete.")
