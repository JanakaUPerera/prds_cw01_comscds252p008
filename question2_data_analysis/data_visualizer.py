"""
data_visualizer.py
This module contains functions to create various visualizations using Plotly only. 
It generates: 
    histogram of book prices with mean line, 
    box plot comparing prices across the top 5 categories, 
    scatter plot of price vs rating with a regression line, 
    bar chart of average ratings by category for the top 8 categories.
    Interactive versions of the scatter plot and bar chart.
        Selectors to choose top categories
The visualizations are saved in the 'data/visualizations' folder as HTML files.
"""

import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

CLEANED_DATA_PATH = "question2_data_analysis/data/cleaned/"
OUT_DATA_PATH = "question2_data_analysis/data/visualizations/"


def histogram_price(df: pd.DataFrame) -> None:
    print(f"\n-- Interactive Histogram: Price distribution with mean line (Plotly) --")

    mean_price = df["price"].mean()

    fig = px.histogram(
        df,
        x="price",
        nbins=20,
        title="Price Distribution of Books",
        labels={"price": "Price (£)", "count": "Frequency"},
    )

    # Mean line
    fig.add_vline(
        x=mean_price,
        line_width=3,
        line_dash="dash",
        annotation_text=f"Mean = £{mean_price:.2f}",
        annotation_position="top right"
    )

    fig.write_html(os.path.join(OUT_DATA_PATH, "histogram_price.html"))


def boxplot_top5_categories(df: pd.DataFrame) -> None:
    print(f"\n-- Interactive Box Plot: Price comparison across top 5 categories (Plotly) --")

    top5 = df["category"].value_counts().head(5).index
    subset = df[df["category"].isin(top5)]

    fig = px.box(
        subset,
        x="category",
        y="price",
        title="Price Comparison Across Top 5 Categories",
        labels={"category": "Category", "price": "Price (£)"},
    )

    fig.update_layout(xaxis_tickangle=-20)

    fig.write_html(os.path.join(OUT_DATA_PATH, "boxplot_price_top5_categories.html"))


def scatterplot_price_vs_rating(df: pd.DataFrame) -> None:
    print(f"\n-- Interactive Scatter Plot: Price vs Rating with regression line (Plotly) --")

    x = df["rating"].values
    y = df["price"].values

    # Regression line
    m, b = np.polyfit(x, y, 1)
    xs = np.linspace(x.min(), x.max(), 100)
    ys = m * xs + b

    fig = go.Figure()

    # Scatter points
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="markers",
        name="Books"
    ))

    # Regression line
    fig.add_trace(go.Scatter(
        x=xs,
        y=ys,
        mode="lines",
        name="Regression Line"
    ))

    fig.update_layout(
        title="Price vs Rating (with Regression Line)",
        xaxis_title="Rating (1–5)",
        yaxis_title="Price (£)"
    )

    fig.write_html(os.path.join(OUT_DATA_PATH, "scatterplot_price_vs_rating.html"))


def bar_avg_rating_top8(df: pd.DataFrame) -> None:
    print(f"\n-- Interactive Bar Chart: Average rating by category (top 8) (Plotly) --")

    top8 = df["category"].value_counts().head(8).index
    subset = df[df["category"].isin(top8)]

    avg_rating = (
        subset.groupby("category")["rating"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        avg_rating,
        x="category",
        y="rating",
        title="Average Rating by Category (Top 8 Categories)",
        labels={"category": "Category", "rating": "Average Rating"},
    )

    fig.update_layout(showlegend=True)

    fig.write_html(os.path.join(OUT_DATA_PATH, "bar_avg_rating_top8.html"))

def interactive_scatterplot_price_vs_rating_selector(df: pd.DataFrame) -> None:
    print(f"\n-- Interactive Scatter Plot: Price vs Rating with selector --")

    # Top categories by frequency
    category_counts = df["category"].value_counts()

    limits = [5, 10, 15, 20, len(category_counts)]
    labels = ["Top 5", "Top 10", "Top 15", "Top 20", "All"]

    fig = go.Figure()

    # Create traces
    for limit, label in zip(limits, labels):
        top_categories = category_counts.head(limit).index
        subset = df[df["category"].isin(top_categories)]

        x = subset["rating"].values
        y = subset["price"].values

        # Regression line
        if len(x) > 1:
            m, b = np.polyfit(x, y, 1)
            xs = np.linspace(x.min(), x.max(), 100)
            ys = m * xs + b
        else:
            xs, ys = [], []

        # Scatter trace
        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode="markers",
            name=f"{label} Books",
            visible=(label == "Top 5"),
            hovertemplate="Rating: %{x}<br>Price: £%{y:.2f}<extra></extra>"
        ))

        # Regression line trace
        fig.add_trace(go.Scatter(
            x=xs,
            y=ys,
            mode="lines",
            name=f"{label} Regression",
            visible=(label == "Top 5")
        ))

    # Dropdown buttons
    buttons = []
    n_traces = len(labels) * 2  # scatter + regression per option

    for i, label in enumerate(labels):
        visibility = [False] * n_traces
        visibility[i*2] = True       # scatter
        visibility[i*2 + 1] = True   # regression

        buttons.append(dict(
            label=label,
            method="update",
            args=[
                {"visible": visibility},
                {"title": f"Price vs Rating ({label} Categories)"}
            ]
        ))

    fig.update_layout(
        title="Price vs Rating (Top 5 Categories)",
        xaxis_title="Rating (1–5)",
        yaxis_title="Price (£)",
        hovermode="closest",
        updatemenus=[
            dict(
                active=0,
                buttons=buttons,
                x=1.15,
                y=0.90
            )
        ]
    )

    fig.write_html(os.path.join(OUT_DATA_PATH, "interactive_scatterplot_price_vs_rating_selector.html"))

def interactive_bar_avg_rating_selector(df: pd.DataFrame) -> None:
    print(f"\n-- Interactive Bar Chart: Average rating by category with selector --")

    avg_rating = (
        df.groupby("category")["rating"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    limits = [5, 10, 15, 20, len(avg_rating)]
    labels = ["Top 5", "Top 10", "Top 15", "Top 20", "All"]

    fig = go.Figure()

    for limit, label in zip(limits, labels):
        subset = avg_rating.head(limit)

        fig.add_trace(go.Bar(
            x=subset["category"],
            y=subset["rating"],
            name=label,
            visible=(label == "Top 5")
        ))

    buttons = []
    for i, label in enumerate(labels):
        visibility = [False] * len(labels)
        visibility[i] = True

        buttons.append(dict(
            label=label,
            method="update",
            args=[
                {"visible": visibility},
                {"title": f"Average Rating by Category ({label})"}
            ]
        ))

    fig.update_layout(
        title="Average Rating by Category (Top 5)",
        xaxis_title="Category",
        yaxis_title="Average Rating",
        updatemenus=[
            dict(
                active=0,
                buttons=buttons,
                x=1.15,
                y=1.0
            )
        ]
    )

    fig.write_html(os.path.join(OUT_DATA_PATH, "interactive_bar_avg_rating_selector.html"))

def data_visualize(file_name: str) -> None:
    file_path = os.path.join(CLEANED_DATA_PATH, file_name)
    df = pd.read_csv(file_path)

    os.makedirs(OUT_DATA_PATH, exist_ok=True)

    histogram_price(df)
    boxplot_top5_categories(df)
    scatterplot_price_vs_rating(df)
    bar_avg_rating_top8(df)
    interactive_scatterplot_price_vs_rating_selector(df)
    interactive_bar_avg_rating_selector(df)

    print("\n-- Interactive Visualizations saved in 'data/visualizations' folder: --")
    print("1) histogram_price.html")
    print("2) boxplot_price_top5_categories.html")
    print("3) scatterplot_price_vs_rating.html")
    print("4) bar_avg_rating_top8.html")
    print("5) interactive_scatterplot_selector.html")
    print("6) interactive_bar_avg_rating_selector.html")


if __name__ == "__main__":
    data_visualize('cleaned_books_data_500.csv')
