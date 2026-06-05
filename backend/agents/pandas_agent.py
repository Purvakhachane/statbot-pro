from analysis.aggregation import (
    perform_aggregation,
    group_by_analysis
)

from analysis.basic_analysis import (
    get_dataset_overview,
    get_numerical_summary
)


from analysis.filtering import apply_filter

def execute_query(df, parsed_query):

    operation = parsed_query.get("operation")
    try:
        # Dataset Overview
        if operation == "overview":
            return get_dataset_overview(df)

        # Numerical Summary
        elif operation == "summary":
            return get_numerical_summary(df)

        # Aggregations
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
                return "Column name is required."

            return perform_aggregation(
                df,
                operation,
                column
            )

        # Group By Analysis
        elif operation == "groupby":
            group_by = parsed_query.get("group_by")
            column = parsed_query.get("column")
            aggregation = parsed_query.get(
                "aggregation",
                "sum"
            )

            return group_by_analysis(
                df,
                group_by,
                column,
                aggregation
            )

        # Filtering
        elif operation == "filter":
            return apply_filter(
                df,
                parsed_query.get("column"),
                parsed_query.get("condition"),
                parsed_query.get("value")
            )

        return f"Unsupported operation: {operation}"

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }