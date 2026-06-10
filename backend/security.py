# security.py

BLOCKED_KEYWORDS = [
    "eval",
    "exec",
    "os.system",
    "subprocess",
    "__import__",
    "open(",
    "rm -rf",
    "shutdown"
]


def validate_query(user_query):

    if not user_query.strip():

        return {
            "status": "error",
            "message": "Empty query is not allowed."
        }

    if len(user_query) > 1000:

        return {
            "status": "error",
            "message": "Query exceeds maximum length."
        }

    query = user_query.lower()

    for keyword in BLOCKED_KEYWORDS:

        if keyword in query:

            return {
                "status": "error",
                "message": f"Blocked keyword detected: {keyword}"
            }

        return {
            "status": "success"
        }

    def log_blocked_query(query):

    with open(
        "security_log.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            query + "\n"
        )

        if keyword in query:

    log_blocked_query(query)

    return {
        "status": "error",
        "message": f"Blocked keyword detected: {keyword}"
    }