import pandas as pd

# Missing values
def get_missing_values(df):
    return df.isnull().sum()


# Dataset shape
def get_dataset_shape(df):
    return {"Rows": df.shape[0], "Columns": df.shape[1]}


# Correlation (safe)
def get_correlation(df):
    numeric_df = df.select_dtypes(include=['number'])
    return numeric_df.corr()


# Summary
def get_dataset_summary(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1]
    }


# Numeric insights (SAFE VERSION)
def get_numeric_insights(df, column):

    if column not in df.columns:
        return {"error": "Column not found"}

    if not pd.api.types.is_numeric_dtype(df[column]):
        return {"error": "Column is not numeric"}

    return {
        "Maximum": df[column].max(),
        "Minimum": df[column].min(),
        "Average": round(df[column].mean(), 2),
        "Median": round(df[column].median(), 2)
    }