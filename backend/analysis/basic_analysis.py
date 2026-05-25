import pandas as pd

def get_dataset_overview(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "data_types": df.dtypes.astype(str).to_dict()
    }


def get_sample_data(df, rows=5):
    return df.head(rows)


def get_numerical_summary(df):
    numeric_df = df.select_dtypes(include=["number"])
    return numeric_df.describe()


def get_unique_values(df, column):
    if column not in df.columns:
        return f"Column '{column}' not found"
    return df[column].unique().tolist()


def get_null_percentage(df):
    null_percentage = (df.isnull().sum() / len(df)) * 100
    return null_percentage.round(2).to_dict()