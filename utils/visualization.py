import matplotlib.pyplot as plt
import pandas as pd

def generate_chart(df, x_col, y_col, chart_type):

    # Create copy to avoid modifying original dataframe
    chart_df = df.copy()

    # Convert to numeric
    chart_df[y_col] = pd.to_numeric(
        chart_df[y_col],
        errors="coerce"
    )

    # Remove null values
    chart_df = chart_df.dropna(
        subset=[y_col]
    )

    # Group data
    grouped_df = (
        chart_df.groupby(x_col)[y_col]
        .sum()
        .head(20)  # Only first 20 groups
    )

    # Create figure
    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    if chart_type == "Line":

        ax.plot(
            grouped_df.index.astype(str),
            grouped_df.values,
            marker="o"
        )

    elif chart_type == "Bar":

        ax.bar(
            grouped_df.index.astype(str),
            grouped_df.values
        )

    elif chart_type == "Scatter":

        ax.scatter(
            grouped_df.index.astype(str),
            grouped_df.values
        )

    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f"{chart_type} Chart")

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig