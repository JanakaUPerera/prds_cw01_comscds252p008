"""
data_analyzer.py
This module contains functions to perform descriptive and inferential statistical analysis.
"""
import os
import pandas as pd
from scipy import stats

CLEANED_DATA_PATH = "question2_data_analysis/data/cleaned/" # Path to save the cleaned data

def analyze_data_descriptive_statistics(file_name: str) -> None:
    file_path = os.path.join(CLEANED_DATA_PATH, file_name)
    df = pd.read_csv(file_path)
    
    # Central tendency: mean, median, mode for prices
    print(f"\n-- Central tendency: Mean, Median, Mode for Price --")
    mean_price = df["price"].mean()
    median_price = df["price"].median()
    mode_price = df["price"].mode()
    print(f"Mean:\t\t{mean_price:.2f}")
    print(f"Median:\t\t{median_price:.2f}")
    if not mode_price.empty:
        print(f"Mode:\t\t{mode_price[0]:.2f}")
        
    # Dispersion: standard deviation, range
    print(f"\n-- Dispersion: standard deviation, range --")
    std_price = df["price"].std()
    price_range = df["price"].max() - df["price"].min()
    print(f"STD:\t\t{std_price:.2f}")
    print(f"Range:\t\t{price_range:.2f}")
    
    #Group statistics: average price by category (top 5)
    print(f"\n-- Group statistics: average price by category (top 5) --")
    top5_categories = (
        df['category']
        .value_counts(ascending=False)
        .head(5)
        .index
    )
    avg_prices_by_category = (
        df[df['category'].isin(top5_categories)]
        .groupby('category')['price']
        .mean()
        .round(2)
        .sort_values(ascending=False)
        .reset_index()
    )
    print(avg_prices_by_category)
    
    # Rating distribution: frequency count
    print(f"\n-- Rating distribution: frequency count --")
    rating_distribution = (
        df["rating"]
        .value_counts()
        .sort_index()
        .reset_index()
    )
    print(rating_distribution)

def analyze_data_inferential_statistics(file_name: str) -> None:
    ALPHA = 0.05  # significance level
    
    file_path = os.path.join(CLEANED_DATA_PATH, file_name)
    df = pd.read_csv(file_path)
    
    # Outlier detection: Use IQR method for price outliers
    print(f"\n-- Outlier detection: Use IQR method for price outliers --")
    Q1 = df["price"].quantile(0.25)
    Q3 = df["price"].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df["price"] < lower_bound) | (df["price"] > upper_bound)]

    print(f"Q1:\t\t\t\t{Q1:.2f}")
    print(f"Q3:\t\t\t\t{Q3:.2f}")
    print(f"IQR:\t\t\t\t{IQR:.2f}")
    print(f"Lower Bound:\t\t\t{lower_bound:.2f}")
    print(f"Upper Bound:\t\t\t{upper_bound:.2f}")
    print(f"Number of Outliers:\t\t{len(outliers)}")

    # Correlation analysis: Pearson correlation between price and rating
    print(f"\n-- Correlation analysis: Pearson correlation between price and rating --")
    correlation, p_corr = stats.pearsonr(df["price"], df["rating"])

    print(f"Pearson Correlation Coefficient (r):\t{correlation:.3f}")
    print(f"P-value:\t\t\t\t{p_corr:.4f}")

    if p_corr < ALPHA:
        print("Conclusion: Significant correlation exists.")
    else:
        print("Conclusion: No statistically significant correlation.")
    
    # Hypothesis testing
    # Compare average prices between Fiction vs Non-Fiction
    print(f"\n-- Hypothesis testing - Compare average prices between Fiction vs Non-Fiction --")
    fiction_prices = df[df["category"] == "Fiction"]["price"]
    nonfiction_prices = df[df["category"] == "Nonfiction"]["price"]
    
    if len(fiction_prices) >= 2 and len(nonfiction_prices) >= 2:

        t_stat, p_value = stats.ttest_ind(
            fiction_prices,
            nonfiction_prices,
            equal_var=False  # Welch's t-test (safer)
        )

        print(f"Fiction Mean Price:\t{fiction_prices.mean():.2f}")
        print(f"Non-Fiction Mean Price:\t{nonfiction_prices.mean():.2f}")
        print(f"T-statistic:\t\t{t_stat:.3f}")
        print(f"P-value:\t\t{p_value:.4f}")

        if p_value < ALPHA:
            print("Conclusion: Significant difference in average prices.")
        else:
            print("Conclusion: No significant difference in average prices.")

    else:
        print("Not enough data to perform t-test.")
    
if __name__ == "__main__":
    # analyze_data_descriptive_statistics('cleaned_books_data_500.csv')
    analyze_data_inferential_statistics('cleaned_books_data_500.csv')
    