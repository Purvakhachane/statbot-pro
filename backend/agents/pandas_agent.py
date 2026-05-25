from analysis.aggregation import (perform_aggregation, group_by_analysis)

from analysis.basic_analysis import (get_dataset_overview, get_numerical_summary)

from analysis.filtering import apply_filter


def execute_query(df, parsed_query):
    operation = parsed_query.get("operation")
    column = parsed_query.get("column")
    condition = parsed_query.get("condition")
    value = parsed_query.get("value")
    group_by = parsed_query.get("group_by")

    try:
        # Dataset Overview
        if operation == "overview":
            return get_dataset_overview(df)

        # Numerical Summary
        elif operation == "summary":
            return get_numerical_summary(df)

        # Aggregation Operations
        elif operation in [
            "sum",
            "mean",
            "max",
            "min",
            "count",
            "median",
            "std"
        ]:
            return perform_aggregation(df, operation, column)

        # Group By Analysis
        elif operation == "groupby":
            return group_by_analysis(
                df,
                group_by,
                column,
                parsed_query.get("aggregation", "sum")
            )

        # Filtering
        elif operation == "filter":
            return apply_filter(df, column, condition, value)

        else:
            return f"Unsupported operation '{operation}'"

    except Exception as e:
        return f"Execution Error: {str(e)}"