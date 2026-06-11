# utils/ai_client.py

def process_query(query):
    print("AI_CLIENT PROCESS_QUERY CALLED")
    query = query.lower()

    if "highest" in query or "max" in query:
        return "Detected operation: Maximum Value Analysis"

    elif "average" in query or "mean" in query:
        return "Detected operation: Average Calculation"

    elif "total" in query or "sum" in query:
        return "Detected operation: Sum Aggregation"

    elif "lowest" in query or "min" in query:
        return "Detected operation: Minimum Value Analysis"

    return "Query received successfully. Waiting for AI engine integration."