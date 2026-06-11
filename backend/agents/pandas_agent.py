from backend.analysis.aggregation import (
    perform_aggregation,
    group_by_analysis
)

from backend.analysis.basic_analysis import (
    get_dataset_overview,
    get_numerical_summary
)

from backend.analysis.filtering import apply_filter

def execute_query(df, parsed_query):
    operation = parsed_query.get("operation")
    try:
        if operation == "overview":
            return get_dataset_overview(df)
        
        elif operation == "summary":
            return get_numerical_summary(df)

        elif operation in [
            "sum",
            "mean",
            "max",
            "min",
            "count",
            "median",
            "std"
        ]:

            column = parsed_query.get("column")

            if not column:
                return {
                    "status": "error",
                    "message": "Column name is required."
                }

            if column not in df.columns:
                return {
                    "status": "error",
                    "message": f"Column '{column}' not found."
                }

            return perform_aggregation(
                df,
                operation,
                column
            )

        elif operation == "groupby":

            group_by = parsed_query.get("group_by")
            column = parsed_query.get("column")

            aggregation = parsed_query.get(
                "aggregation",
                "sum"
            )

            if group_by not in df.columns:
                return {
                    "status": "error",
                    "message": f"Group column '{group_by}' not found."
                }

            if column not in df.columns:
                return {
                    "status": "error",
                    "message": f"Column '{column}' not found."
                }

            return group_by_analysis(
                df,
                group_by,
                column,
                aggregation
            )

        elif operation == "filter":

            column = parsed_query.get("column")

            if column not in df.columns:
                return {
                    "status": "error",
                    "message": f"Column '{column}' not found."
                }

            return apply_filter(
                df,
                column,
                parsed_query.get("condition"),
                parsed_query.get("value")
            )

        return {
            "status": "error",
            "message": f"Unsupported operation '{operation}'"
        }

    except Exception as error:
        return {
            "status": "error",
            "message": str(error)
        }