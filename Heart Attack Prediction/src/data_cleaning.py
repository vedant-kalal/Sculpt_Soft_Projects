from .config import raw_data_input_path, clean_data_output_path
import pandas as pd

def clean_data(raw_data_input_path, clean_data_output_path):
    df = pd.read_csv(raw_data_input_path)
    df.drop_duplicates(inplace=True)
    df.drop(columns=["Patient ID", "Income", "Country", "Continent", "Hemisphere"], inplace=True, errors='ignore')
    
    if 'Blood Pressure' in df.columns:
        df[['Systolic BP', 'Diastolic BP']] = df['Blood Pressure'].str.split('/', expand=True).astype(float)
        df.drop(columns=['Blood Pressure'], inplace=True)

    df.to_csv(clean_data_output_path, index=False)
    


