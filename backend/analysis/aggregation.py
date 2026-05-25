import pandas as pd

def perform_aggregation(df, operation, column):
    if column not in df.columns:
        return f"Column '{column}' not found"
    
    try:
        numeric_column = pd.to_numeric(
            df[column],
            errors="coerce"
        )

        operations = {
            "sum": numeric_column.sum,
            "mean": numeric_column.mean,
            "max": numeric_column.max,
            "min": numeric_column.min,
            "count": numeric_column.count,
            "median": numeric_column.median,
            "std": numeric_column.std
        }

        if operation not in operations:
            return f"Unsupported operation '{operation}'"

        return operations[operation]()

    except Exception as e:
        return f"Aggregation Error: {str(e)}"



def group_by_analysis(df, group_column, target_column, operation="sum"):
    if group_column not in df.columns:
        return f"Column '{group_column}' not found"

    if target_column not in df.columns:
        return f"Column '{target_column}' not found"

    try:
        grouped = (
            df.groupby(group_column)[target_column]
        )

        operations = {
            "sum": grouped.sum,
            "mean": grouped.mean,
            "max": grouped.max,
            "min": grouped.min,
            "count": grouped.count
        }

        if operation not in operations:
            return f"Unsupported operation '{operation}'"

        return operations[operation]()

    except Exception as e:
        return f"GroupBy Error: {str(e)}"