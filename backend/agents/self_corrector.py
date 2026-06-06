import json

from backend.agents.gemini_agent import get_gemini_model

MAX_RETRIES = 3

def correct_query(
    user_query,
    previous_query,
    error_message,
    available_columns
):
    """
    Ask Gemini to repair a failed query.
    """
    model = get_gemini_model()
    prompt = f"""
You are a data analysis query repair assistant.

User Question:
{user_query}

Failed Query:
{json.dumps(previous_query)}

Error:
{error_message}

Available Columns:
{available_columns}

Rules:
1. Return JSON only.
2. Keep the original intent.
3. Use only available columns.
4. Do not explain anything.
"""

    response = model.invoke(prompt)
    
    cleaned_response = (
        response.content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned_response)