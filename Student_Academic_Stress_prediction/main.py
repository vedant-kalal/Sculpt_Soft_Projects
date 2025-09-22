# Entry point for ML project
import pandas as pd
from data_cleaning import clean_data
from preprocessing_pipeline import build_pipeline, train_and_save_pipeline, visualize_pipeline

if __name__ == "__main__":
    print(" Step 1: Cleaning data...")
    clean_data()

    print("Step 1: Building pipeline...")
    pipeline, X, y = build_pipeline()

    print("Step 2: Training and saving pipeline...")
    train_and_save_pipeline(pipeline, X, y)

    print("Step 3: Visualizing pipeline...")
    visualize_pipeline(pipeline)

    print("✅ Done!")

    # The column names are stored in the preprocessor inside pipeline
    preprocessor = pipeline.named_steps['preprocessor']
    num_features = preprocessor.transformers_[0][2]  # numeric
    cat_features = preprocessor.transformers_[1][2]  # categorical
    feature_names = num_features + cat_features

    # 3️⃣ Ask user for input
    print("\nEnter student data to predict Academic Stress Index:")

    user_input = {}
    for feature in feature_names:
        val = input(f"{feature}: ")
        # Convert numeric features automatically
        if feature in num_features:
            try:
                val = float(val)
                if val.is_integer():
                    val = int(val)
            except:
                pass
        user_input[feature] = [val]  # make it 2D for DataFrame

    user_df = pd.DataFrame(user_input)

    # 4️⃣ Predict using the loaded pipeline
    prediction = pipeline.predict(user_df)

    print(f"\n Predicted Academic Stress Index: {prediction[0]}")