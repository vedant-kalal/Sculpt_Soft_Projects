import pandas as pd
import pickle

# Load the preprocessor and the model
try:
    with open('preprocessor.pkl', 'rb') as f:
        preprocessor = pickle.load(f)
    with open('Fraud_Detection_Model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("Error: Model or preprocessor files not found.")
    print("Please run the updated cell in the 'pipeline.ipynb' notebook to generate 'preprocessor.pkl' and 'fraud_model.pkl'.")
    exit()

def predict_fraud():
    """
    Takes user input for transaction details, preprocesses it,
    and predicts if it's fraudulent.
    """
    print("--- New Fraud Prediction ---")
    print("Please enter the transaction details below.")

    # --- Collect User Input ---
    # These features must match the columns used during model training.
    category = input("Enter transaction category (e.g., 'misc_net', 'grocery_pos'): ")
    gender = input("Enter gender ('M' or 'F'): ")
    amt = float(input("Enter transaction amount (e.g., 50.25): "))
    city = input("Enter city (e.g., 'Abilene'): ")
    city_pop = int(input("Enter city population (e.g., 333497): "))
    job = input("Enter job title (e.g., 'Psychologist, clinical'): ")
    
    # The 'age' column was derived from 'dob' in the original data.
    # We will ask for it directly here.
    age = int(input("Enter customer's age: "))

    # --- Create DataFrame ---
    # The column order must exactly match the order expected by the preprocessor.
    # Based on your notebook, the order is: ['category', 'gender', 'amt', 'city', 'city_pop', 'job', 'age']
    input_data = pd.DataFrame({
        'category': [category],
        'gender': [gender],
        'amt': [amt],
        'city': [city],
        'city_pop': [city_pop],
        'job': [job],
        'age': [age]
    })

    print("\nProcessing input...")
    # --- Preprocess and Predict ---
    # Use the loaded preprocessor to transform the input data
    input_processed = preprocessor.transform(input_data)

    # Use the loaded model to make a prediction
    prediction = model.predict(input_processed)
    prediction_proba = model.predict_proba(input_processed)

    # --- Display Result ---
    print("\n--- Prediction Result ---")
    if prediction[0] == 1:
        print(f"The transaction is likely FRAUDULENT with a probability of {prediction_proba[0][1]:.2%}.")
    else:
        print(f"The transaction is likely NOT fraudulent (Probability of fraud: {prediction_proba[0][1]:.2%}).")

if __name__ == "__main__":
    predict_fraud()
