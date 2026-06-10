import json

from backend.agents.gemini_agent import get_gemini_model

def interpret_query(user_query):
    model = get_gemini_model()
    prompt = f"""
You are a CSV Data Analysis Assistant.
Convert the user query into JSON format.

Allowed operations:
overview
sample_data
summary
null_percentage
unique_values
sum
mean
max
min
count
median
std
filter
groupby
correlation_matrix

Rules:
1. Return ONLY JSON.
2. Do not add explanations.
3. Do not use markdown.
4. Column names must be returned exactly as mentioned.

Examples:
User:
What is the average Revenue?
Output:
{{
    "operation": "mean",
    "column": "Revenue"
}}

User:
Show total Sales
Output:
{{
    "operation": "sum",
    "column": "Sales"
}}

User:
Count all rows
Output:
{{
    "operation": "count"
}}

User:
Show sample data
Output:
{{
    "operation": "sample_data"

}}

User:
Show missing value percentage
Output:
{{
    "operation": "null_percentage"
}}

User:
Show unique values in Region
Output:
{{
    "operation": "unique_values",
    "column": "Region"
}}

User:
Show correlation matrix
Output:
{{
    "operation": "correlation_matrix"
}}

User:
Find relationships between numeric columns
Output:
{{
    "operation": "correlation_matrix"
}}

User:
Which columns are strongly correlated?
Output:
{{
    "operation": "correlation_matrix"
}}

User:
{user_query}
"""
    response = model.invoke(prompt)
    response_text = response.content
    response_text = (
        response_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )
    parsed_query = json.loads(response_text)
    return parsed_query