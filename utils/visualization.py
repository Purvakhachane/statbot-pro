import matplotlib.pyplot as plt
import pandas as pd
import os

def generate_chart(df, x_col, y_col, chart_type):

    os.makedirs("charts", exist_ok=True)

    # Convert numeric column
    df[y_col] = pd.to_numeric(
        df[y_col],
        errors="coerce"
    )

    # Remove nulls
    df = df.dropna(subset=[y_col])

    # Group data
    grouped_df = df.groupby(x_col)[y_col].sum()

    plt.figure(figsize=(8, 5))

    if chart_type == "Line":
        plt.plot(
            grouped_df.index,
            grouped_df.values,
            marker="o"
        )

    elif chart_type == "Bar":
        plt.bar(
            grouped_df.index.astype(str),
            grouped_df.values
        )

    elif chart_type == "Scatter":
        plt.scatter(
            grouped_df.index,
            grouped_df.values
        )

    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.title(f"{chart_type} Chart")

    plt.xticks(rotation=45)

    plt.tight_layout()

    chart_path = "charts/dynamic_chart.png"

    plt.savefig(chart_path)

    plt.close()

    return chart_path