
import pandas as pd
import joblib
import os
from src.data_cleaning import clean_data
from src.train_pipeline import build_pipeline, train_and_evaluate, visualize_pipeline, save_pipeline
from src.config import model_output_path, clean_data_output_path, raw_data_input_path

print("Cleaning data...")
try:
    clean_data(raw_data_input_path, clean_data_output_path)
    print("Data cleaned successfully.")
except Exception as e:
    print(f"Error occurred while cleaning data: {e}")
    exit(1)


print("Building and training pipeline...")
try:
    pipeline, X, y = build_pipeline()
    print("Pipeline built and trained successfully.")
except Exception as e:
    print(f"Error occurred while building/training pipeline: {e}")
    exit(1)

print("Visualizing pipeline...")
try:
    visualize_pipeline(pipeline)
except Exception as e:
    print(f"Error occurred while visualizing pipeline: {e}")
    exit(1)

print("Training and evaluating pipeline...")
try:
    train_and_evaluate(pipeline, X, y)
    print("Pipeline trained and evaluated successfully.")
except Exception as e:
    print(f"Error occurred while training/evaluating pipeline: {e}")


print("Saving pipeline...")
try:
    save_pipeline(pipeline)
    print("Pipeline saved successfully.")
except Exception as e:
    print(f"Error occurred while saving pipeline: {e}")
    exit(1)

print("All steps completed successfully.")


try:
    trained_pipeline = joblib.load(model_output_path)
    print("Trained pipeline loaded successfully for verification.")
except Exception as e:
    print(f"Error occurred while loading trained pipeline: {e}")
    exit(1)

expected_columns = [
            'Age', 'Sex', 'Cholesterol', 'Heart Rate', 'Diabetes', 'Family History', 'Smoking', 'Obesity',
            'Alcohol Consumption', 'Exercise Hours Per Week', 'Diet', 'Previous Heart Problems', 'Medication Use',
            'Stress Level', 'Sedentary Hours Per Day', 'BMI', 'Triglycerides', 'Physical Activity Days Per Week',
            'Sleep Hours Per Day', 'Systolic BP', 'Diastolic BP'
        ]

print("Enter Patient Details for Heart Attack Prediction:")

check_binary_data={"yes":1,"no":0}
prediction_check={1:"There is a high risk of Heart Attack",0:"There is a low risk of Heart Attack"}
age = float(input("Enter Age of Patient: "))
sex = input("Enter Sex of Patient (Male/Female): ").capitalize()
cholesterol = float(input("Enter Cholesterol Level: "))
heart_rate = float(input("Enter Heart Rate: "))
diabetes = input("Does the patient have Diabetes? (yes/no): ").lower()
family_history = input("Is there a Family History of Heart Disease? (yes/no): ").lower()
smoking = input("Is the patient a Smoker? (yes/no): ").lower()
obesity = input("Is the patient Obese? (yes/no): ").lower()
alcohol_consumption = input("patient consumes Alcohol? (yes/no): ").lower()
exercise_hours = float(input("Enter Exercise Hours Per Week: "))
diet = input("Is the patient's Diet Healthy? (Healthy/Unhealthy/Average): ").capitalize()
previous_problems = input("Has the patient had Previous Heart Problems? (yes/no): ").lower()
medication_use = input("Is the patient on Medication? (yes/no): ").lower()
stress_level = float(input("Enter Stress Level (1-10): "))
sedentary_hours = float(input("Enter Sedentary Hours Per Day: "))
bmi = float(input("Enter BMI: "))
triglycerides = float(input("Enter Triglycerides Level: "))
physical_activity_days = float(input("Enter Physical Activity Days Per Week: "))
sleep_hours = float(input("Enter Sleep Hours Per Day: "))
systolic_bp = float(input("Enter Systolic Blood Pressure: "))
diastolic_bp = float(input("Enter Diastolic Blood Pressure: "))

data = {
    "Age": [age],
    "Sex": [sex],
    "Cholesterol": [cholesterol],
    "Heart Rate": [heart_rate],
    "Diabetes": [check_binary_data[diabetes]],
    "Family History": [check_binary_data[family_history]],
    "Smoking": [check_binary_data[smoking]],
    "Obesity": [check_binary_data[obesity]],
    "Alcohol Consumption": [check_binary_data[alcohol_consumption]],
    "Exercise Hours Per Week": [exercise_hours],
    "Diet": [diet],
    "Previous Heart Problems": [check_binary_data[previous_problems]],
    "Medication Use": [check_binary_data[medication_use]],
    "Stress Level": [stress_level],
    "Sedentary Hours Per Day": [sedentary_hours],
    "BMI": [bmi],
    "Triglycerides": [triglycerides],
    "Physical Activity Days Per Week": [physical_activity_days],
    "Sleep Hours Per Day": [sleep_hours],
    "Systolic BP": [systolic_bp],
    "Diastolic BP": [diastolic_bp]
}
user_df = pd.DataFrame(data)

try:
    user_proc = trained_pipeline.named_steps['preprocessor'].transform(user_df)
    prediction = trained_pipeline.named_steps['model'].predict(user_proc)
    print(f"\nPredicted Heart Attack Risk: {prediction_check[prediction[0]]}")
except Exception as e:
    print("Trained pipeline not found. Please train the model first.")