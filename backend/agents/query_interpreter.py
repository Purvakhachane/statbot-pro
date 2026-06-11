import json

from backend.agents.gemini_agent import get_gemini_model

def interpret_query(user_query):
    model = get_gemini_model()
    prompt = f"""
You are a CSV Data Analysis Assistant.
Convert the user query into JSON format.

Allowed operations:
overview
summary
sum
mean
max
min
count
median
std
filter
groupby

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