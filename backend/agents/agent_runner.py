from backend.agents.query_interpreter import interpret_query
from backend.agents.pandas_agent import execute_query
from backend.agents.self_corrector import correct_query
from backend.security import validate_query

MAX_RETRIES = 3

def run_agent(df, user_query):

    security_check = validate_query(user_query)

    if security_check["status"] == "error":

        return security_check


    try:
        parsed_query = interpret_query(user_query)
        attempt = 0

        while attempt < MAX_RETRIES:
            result = execute_query(df, parsed_query)

            if not (
                isinstance(result, dict)
                and result.get("status") == "error"
            ):

                return {
                    "status": "success",
                    "query": user_query,
                    "parsed_query": parsed_query,
                    "result": result
                }

            parsed_query = correct_query(
                user_query=user_query,
                previous_query=parsed_query,
                error_message=result.get("message"),
                available_columns=list(df.columns)
            )

            attempt += 1

        return {
            "status": "error",
            "message": "Unable to answer the query using the uploaded dataset.",
            "available_columns": list(df.columns),
            "attempts": MAX_RETRIES
        }

    except Exception as error:
        return {
            "status": "error",
            "message": str(error)
        }