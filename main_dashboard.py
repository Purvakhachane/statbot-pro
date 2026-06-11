import streamlit as st
import pandas as pd

from utils.file_handler import save_uploaded_file
from utils.data_preview import load_csv
from utils.visualization import generate_chart
from backend.agents.agent_runner import run_agent


def show_dashboard():

    if "query_history" not in st.session_state:
        st.session_state.query_history = []

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = True

    if "username" not in st.session_state:
        st.session_state.username = "User"

    # ---------------- SIDEBAR ---------------- #
    st.sidebar.title("StatBot Pro")
    st.sidebar.info("AI Powered CSV Data Analyst")
    st.sidebar.markdown("---")

    st.sidebar.write("Upload your CSV dataset and explore insights instantly.")
    st.sidebar.success(f"Welcome, {st.session_state.username}")
    st.sidebar.markdown("---")

    if st.sidebar.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    # ---------------- MAIN ---------------- #
    st.title("📊 StatBot Pro")
    st.subheader("Autonomous CSV Data Analyst")

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is None:
        st.info("Please upload a CSV file to continue.")
        return

    try:
        file_path = save_uploaded_file(uploaded_file)
        st.success("File uploaded successfully!")

        st.subheader("File Information")
        st.write(f"File Name: {uploaded_file.name}")
        st.write(f"File Size: {uploaded_file.size / 1024:.2f} KB")

        df = load_csv(file_path)

        # ---------------- TABS ---------------- #
        tab1, tab2, tab3 = st.tabs(
            ["📄 Dataset", "📈 Visualizations", "🤖 AI Assistant"]
        )

        # ================= DATASET TAB ================= #
        with tab1:
            st.subheader("Column Filter")

            selected_columns = st.multiselect(
                "Choose columns to display",
                df.columns,
                default=list(df.columns)
            )

            filtered_df = df[selected_columns]

            st.subheader("Dataset Preview")
            st.dataframe(filtered_df.head(), use_container_width=True)

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Rows", df.shape[0])
            col2.metric("Columns", df.shape[1])
            col3.metric("Missing Values", int(df.isnull().sum().sum()))
            col4.metric("Duplicate Rows", int(df.duplicated().sum()))

            st.subheader("Search Dataset")
            search_term = st.text_input("Search value")

            if search_term:
                search_results = filtered_df[
                    filtered_df.astype(str).apply(
                        lambda row: row.str.contains(search_term, case=False).any(),
                        axis=1
                    )
                ]

                st.write(f"Found {len(search_results)} matching rows")
                st.dataframe(search_results, use_container_width=True)

            st.subheader("Dataset Information")
            st.write(df.dtypes)

            st.subheader("Missing Values")
            st.write(df.isnull().sum())

            if st.button("Generate Data Quality Report"):
                st.write(df.isnull().sum())
                st.write(f"Duplicate Rows: {df.duplicated().sum()}")

            if st.button("Generate Dataset Summary"):
                st.write(df.describe())

        # ================= VISUALIZATION TAB ================= #
        with tab2:
            st.subheader("Data Visualization")

            x_col = st.selectbox("Select X-axis Column", df.columns)
            y_col = st.selectbox("Select Y-axis Column", df.columns)

            chart_type = st.selectbox(
                "Select Chart Type",
                ["Line", "Bar", "Scatter"]
            )

            if st.button("Generate Chart"):
                fig = generate_chart(df, x_col, y_col, chart_type)
                st.pyplot(fig)

        # ================= AI TAB ================= #
        with tab3:
            st.subheader("AI Dataset Assistant")

            user_query = st.text_input("Ask a question about your dataset")

            if st.button("Analyze Query"):
                if user_query.strip() == "":
                    st.warning("Please enter a query.")
                else:
                    response = run_agent(df, user_query)

                    st.session_state.query_history.append(user_query)

                    if isinstance(response, dict):
                        if response.get("status") == "success":
                            st.success("Query executed successfully")
                            if "result" in response:
                                st.write(response["result"])
                        else:
                            st.error(response.get("message", "Unknown error"))
                    else:
                        st.write(response)

            if st.session_state.query_history:
                st.subheader("Query History")
                for q in reversed(st.session_state.query_history):
                    st.write(f"• {q}")

            if st.button("Clear History"):
                st.session_state.query_history = []
                st.rerun()

    except Exception as e:
        st.error(f"Error: {e}")

    st.markdown("---")
    st.caption("StatBot Pro | Internship Project")