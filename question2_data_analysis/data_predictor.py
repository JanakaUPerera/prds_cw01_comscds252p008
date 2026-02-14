"""
data_predictor.py
This module performs predictive analysis using linear regression.
It predicts book prices based on features like rating and category.
The model is evaluated using R² score and Mean Absolute Error (MAE).
Feature importance is also analyzed to understand which features influence price the most.
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

CLEANED_DATA_PATH = "question2_data_analysis/data/cleaned/" # Path to save the cleaned data

def predict_data(file_name: str) -> None:
    file_path = os.path.join(CLEANED_DATA_PATH, file_name)
    df = pd.read_csv(file_path)
    
    # Predictive Analysis (Linear Regression)

    # Define Features and Target
    X = df[["rating", "category"]].copy()
    y = df["price"]

    # One-hot encode category
    X = pd.get_dummies(X, columns=["category"], drop_first=True)

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Evaluation
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)

    print(f"R² Score:\t\t\t{r2:.3f}")
    print(f"Mean Absolute Error (MAE):\t{mae:.3f}")

    # Feature Importance (Coefficients)
    coefficients = pd.Series(model.coef_, index=X.columns)
    coefficients_sorted = coefficients.sort_values(key=lambda x: abs(x), ascending=False)

    print("\n-- Feature Influence (sorted by strength): --")
    print(coefficients_sorted.head(10))


if __name__ == "__main__":
    predict_data('cleaned_books_data_500.csv')
