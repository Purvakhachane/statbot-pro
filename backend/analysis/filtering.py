import pandas as pd

def apply_filter(df, column, condition, value):
    if column not in df.columns:
        return f"Column '{column}' not found"

    try:
        if condition == "greater_than":
            filtered_df = df[df[column] > value]

        elif condition == "less_than":
            filtered_df = df[df[column] < value]

        elif condition == "equal":
            filtered_df = df[df[column] == value]

        elif condition == "not_equal":
            filtered_df = df[df[column] != value]

        else:
            return f"Unsupported condition '{condition}'"

        return filtered_df

    except Exception as e:
        return f"Filtering Error: {str(e)}"