"""
data_visualizer.py
This module contains functions to create various visualizations. 
It generates: 
    Histogram of book prices, 
    Box plot comparing prices across the top 5 categories, 
    Scatter plot of price vs rating with a regression line, 
    Interactive bar chart of average ratings by category for the top 8 categories. 
The visualizations are saved in the 'data/visualizations' folder.
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

CLEANED_DATA_PATH = "question2_data_analysis/data/cleaned/" # Path to save the cleaned data
OUT_DATA_PATH = "question2_data_analysis/data/visualizations/" # Path to save the charts and graphs

def histogram_price(df: pd.DataFrame) -> None:
    # Histogram: Price distribution with mean line (Matplotlib).
    print(f"\n-- Histogram: Price distribution with mean line (Matplotlib). --")
    plt.figure()
    plt.hist(df["price"], bins=20, label="Book Prices")
    mean_price = df["price"].mean()
    plt.axvline(mean_price, linewidth=2, label=f"Mean = £{mean_price:.2f}")

    plt.title("Price Distribution of Books")
    plt.xlabel("Price (£)")
    plt.ylabel("Frequency")
    plt.legend()

    plt.savefig(os.path.join(OUT_DATA_PATH, "histogram_price.png"), dpi=200)
    plt.close()


def boxplot_top5_categories(df: pd.DataFrame) -> None:
    # Box plot: Price comparison across top 5 categories (Matplotlib)
    print(f"\n-- Box plot: Price comparison across top 5 categories (Matplotlib) --")
    top5 = df["category"].value_counts().head(5).index
    subset = df[df["category"].isin(top5)]

    data = [subset[subset["category"] == c]["price"].values for c in top5]

    plt.figure()
    plt.boxplot(data, tick_labels=top5)

    plt.title("Price Comparison Across Top 5 Categories")
    plt.xlabel("Category")
    plt.ylabel("Price (£)")

    # Legend workaround for boxplot (Matplotlib doesn’t auto-legend boxplots nicely)
    plt.plot([], [], label="Price distribution (Box plot)")
    plt.legend()

    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()

    plt.savefig(os.path.join(OUT_DATA_PATH, "boxplot_price_top5_categories.png"), dpi=200)
    plt.close()


def scatterplot_price_vs_rating(df: pd.DataFrame) -> None:
    # Scatter plot: Price vs Rating with regression line (Matplotlib).
    print(f"\n-- Scatter plot: Price vs Rating with regression line (Matplotlib). --")
    x = df["rating"].values
    y = df["price"].values

    plt.figure()
    plt.scatter(x, y, label="Books")

    # Regression line
    m, b = np.polyfit(x, y, 1)
    xs = np.linspace(x.min(), x.max(), 100)
    plt.plot(xs, m * xs + b, linewidth=2, label="Regression line")

    plt.title("Price vs Rating (with Regression Line)")
    plt.xlabel("Rating (1–5)")
    plt.ylabel("Price (£)")
    plt.legend()

    plt.savefig(os.path.join(OUT_DATA_PATH, "scatterplot_price_vs_rating.png"), dpi=200)
    plt.close()


def interactive_bar_avg_rating_top8(df: pd.DataFrame) -> None:
    # Bar chart: Average rating by category (top 8)
    print(f"\n-- Bar chart: Average rating by category (top 8) --")
    top8 = df["category"].value_counts().head(8).index
    subset = df[df["category"].isin(top8)]

    avg_rating = (
        subset.groupby("category")["rating"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    # Make this interactive using Plotly
    fig = px.bar(
        avg_rating,
        x="category",
        y="rating",
        title="Average Rating by Category (Top 8 Categories)",
        labels={"category": "Category", "rating": "Average Rating"},
    )

    # Plotly legend is automatic; we just ensure it's visible
    fig.update_layout(showlegend=True)

    # Save interactive HTML
    fig.write_html(os.path.join(OUT_DATA_PATH, "interactive_bar_avg_rating_top8.html"))


def data_visualize(file_name:str) -> None:
    file_path = os.path.join(CLEANED_DATA_PATH, file_name)
    df = pd.read_csv(file_path)
    
    os.makedirs(OUT_DATA_PATH, exist_ok=True) # If the path is not exist, create the path 

    histogram_price(df)
    boxplot_top5_categories(df)
    scatterplot_price_vs_rating(df)
    interactive_bar_avg_rating_top8(df)

    print("\n-- Visualizations saved in the 'data/visualizations' folder: --")
    print("1) histogram_price.png")
    print("2) boxplot_price_top5_categories.png")
    print("3) scatterplot_price_vs_rating.png")
    print("4) interactive_bar_avg_rating_top8.html")


if __name__ == "__main__":
    data_visualize('cleaned_books_data_500.csv')
