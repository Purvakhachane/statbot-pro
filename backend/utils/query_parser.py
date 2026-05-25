from backend.query_mapping import QUERY_MAP

# DETECT OPERATION
def detect_operation(user_query):
    user_query = user_query.lower()
    for keyword, operation in QUERY_MAP.items():
        if keyword in user_query:
            return operation
    return None


# DETECT COLUMN
def detect_column(user_query, columns):
    user_query = user_query.lower()
    for column in columns:
        if column.lower() in user_query:
            return column
    return None


# DETECT GROUPBY COLUMN
def detect_groupby_column(user_query, columns):
    user_query = user_query.lower()
    words = user_query.split()
    if "by" in words:
        by_index = words.index("by")
        if by_index + 1 < len(words):
            possible_column = words[by_index + 1]
            for column in columns:
                if column.lower() == possible_column.lower():
                    return column
    return None


# DETECT FILTER VALUE
def detect_filter_value(user_query, df):
    user_query = user_query.lower()
    for column in df.columns:
        unique_values = df[column].astype(str).unique()
        for value in unique_values:
            if str(value).lower() in user_query:
                return column, value
    return None, None


# COMPLETE QUERY ANALYSIS
def analyze_query(user_query, df):
    columns = df.columns
    operation = detect_operation(user_query)
    column = detect_column(user_query, columns)
    groupby_column = detect_groupby_column(user_query, columns)
    filter_column, filter_value = detect_filter_value(user_query, df)

    return {
        "operation": operation,
        "column": column,
        "groupby_column": groupby_column,
        "filter_column": filter_column,
        "filter_value": filter_value
    }