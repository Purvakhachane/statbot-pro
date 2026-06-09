# security.py

import streamlit as st


def validate_file(uploaded_file):

    if uploaded_file is None:
        return False

    allowed_extensions = ["csv"]

    extension = uploaded_file.name.split(".")[-1].lower()

    if extension not in allowed_extensions:

        st.error("Only CSV files are allowed.")
        return False

    return True


    def validate_file_size(uploaded_file):

    MAX_SIZE = 5 * 1024 * 1024

    if uploaded_file.size > MAX_SIZE:

        st.error(
            "File size must be less than 5 MB."
        )

        return False

    return True

    def validate_query(user_query):

    blocked_keywords = [

        "eval",
        "exec",
        "os.system",
        "subprocess",
        "__import__",
        "open(",
        "rm -rf",
        "shutdown"

    ]

    query = user_query.lower()

    for keyword in blocked_keywords:

        if keyword in query:

            st.error(
                "Unsafe query detected."
            )

            return False

    return True