import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn import set_config
from config import CLEAN_DATA_PATH, PIPELINE_PATH,target_col

def build_pipeline():
    # Load cleaned data
    df = pd.read_csv(CLEAN_DATA_PATH)
    df.columns = df.columns.str.strip()

    # Features and target
    X = df.drop(columns=[target_col], errors="ignore")
    y = df[target_col]

    # Identify feature types
    num_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_features = X.select_dtypes(include=['object']).columns.tolist()

    # Define transformers
    numeric_transformer = Pipeline(steps=[
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    # Preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, num_features),
            ("cat", categorical_transformer, cat_features)
        ]
    )

    # Full pipeline = preprocessing + model
    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ))
    ])

    # Enable pipeline visualization
    set_config(display="diagram")

    return pipeline, X, y


def train_and_save_pipeline(pipeline, X, y):
    """Fit the pipeline with RandomForest and save as pickle."""
    pipeline.fit(X, y)
    joblib.dump(pipeline, PIPELINE_PATH)
    print(f"✅ Preprocessing + RandomForest pipeline saved at {PIPELINE_PATH}")


def visualize_pipeline(pipeline):
    """Prints pipeline structure."""
    print(pipeline)


if __name__ == "__main__":
    pipeline, X, y = build_pipeline()
    train_and_save_pipeline(pipeline, X, y)
    visualize_pipeline(pipeline)
