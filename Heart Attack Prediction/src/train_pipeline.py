import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn import set_config
from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from .config import clean_data_output_path,model_output_path,TARGET_COL


CLEAN_DATA_PATH = clean_data_output_path
PIPELINE_PATH = model_output_path



def build_pipeline():
    numeric_features = [
        "Age",
        "Cholesterol",
        "Heart Rate",
        "Exercise Hours Per Week",
        "Stress Level",
        "Sedentary Hours Per Day",
        "BMI",
        "Triglycerides",
        "Physical Activity Days Per Week",
        "Sleep Hours Per Day",
        "Systolic BP",
        "Diastolic BP"
    ]
    categorical_features = ["Sex","Diet"]
    df=pd.read_csv(CLEAN_DATA_PATH)
    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]
    
    numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])
    categorical_transformer = Pipeline(steps=[("onehot", OneHotEncoder(handle_unknown="ignore", drop='first'))])

    ColumnTransformers = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features)
        ],
        remainder="passthrough"
    )
    model = RandomForestClassifier( n_estimators=1500,
            min_samples_split=2,
            min_samples_leaf=1,
            max_features='sqrt',
            bootstrap=True,
            class_weight=None,
            random_state=42,
            criterion='gini' 
        )

    Pipelines = Pipeline(steps=[
        ("preprocessor", ColumnTransformers),
        ("model", model)
    ])

    set_config(display="diagram")
    return Pipelines, X, y

def train_and_evaluate(Pipelines, X, y):
    x_processed = Pipelines.named_steps["preprocessor"].fit_transform(X)
    smote = SMOTE(random_state=42)
    x_res , y_res = smote.fit_resample(x_processed, y)
    X_train, X_test, y_train, y_test = train_test_split(x_res, y_res, test_size=0.2, random_state=42)
    Pipelines.named_steps["model"].fit(X_train, y_train)
    y_pred = Pipelines.named_steps["model"].predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(f"Accuracy: {accuracy}")
    print(f"Classification Report: {report}")


def save_pipeline(Pipelines):
    joblib.dump(Pipelines, PIPELINE_PATH)
    print(f"Pipeline saved to {PIPELINE_PATH}")

def visualize_pipeline(Pipelines):
    print(Pipelines)



