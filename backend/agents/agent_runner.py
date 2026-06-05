from backend.agents.query_interpreter import interpret_query
from backend.agents.pandas_agent import execute_query

def run_agent(df, user_query):
    try:
        parsed_query = interpret_query(user_query)
        result = execute_query( df, parsed_query)

        return {
            "status": "success",
            "query": user_query,
            "parsed_query": parsed_query,
            "result": result
        }

    except Exception as error:
        return {
            "status": "error",
            "message": str(error)
        }