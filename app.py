import streamlit as st
import pandas as pd
import os

from utils.file_handler import save_uploaded_file
from utils.data_preview import load_csv
from utils.visualization import generate_chart
from utils.ai_client import process_query

# ---------------- SESSION STATE ---------------- #

if "query_history" not in st.session_state:
    st.session_state.query_history = []

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="StatBot Pro",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.stButton > button {
    background-color: #4F46E5;
    color: white;
    border-radius: 10px;
}

.stDownloadButton > button {
    background-color: #10B981;
    color: white;
    border-radius: 10px;
}

div[data-testid="metric-container"] {
    background-color: white;
    border-radius: 12px;
    padding: 15px;
    border: 1px solid #e6e6e6;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("StatBot Pro")

st.sidebar.info(
    "AI Powered CSV Data Analyst"
)

st.sidebar.markdown("---")

st.sidebar.write(
    "Upload your CSV dataset and explore insights instantly."
)

# ---------------- HEADER ---------------- #

st.title("📊 StatBot Pro")

st.subheader(
    "Autonomous CSV Data Analyst"
)

# ---------------- FILE UPLOADER ---------------- #

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# ---------------- MAIN APP ---------------- #

if uploaded_file is not None:

    try:

        # Save uploaded file
        file_path = save_uploaded_file(uploaded_file)

        st.success("File uploaded successfully!")
        st.subheader("File Information")

        st.write(
            f"File Name: {uploaded_file.name}"
        )

        st.write(
            f"File Size: {uploaded_file.size / 1024:.2f} KB"
        )


        # Load dataset
        df = load_csv(file_path)

        # Tabs
        tab1, tab2, tab3 = st.tabs(
            [
                "📄 Dataset",
                "📈 Visualizations",
                "🤖 AI Assistant"
            ]
        )

        # =====================================================
        # DATASET TAB
        # =====================================================

        with tab1:
            st.subheader("Column Filter")

            selected_columns = st.multiselect(
                "Choose columns to display",
                df.columns,
                default=list(df.columns)
            )

            filtered_df = df[selected_columns]

            st.subheader("Dataset Preview")

            st.dataframe(
                filtered_df.head(),
                use_container_width=True
            )


            col1, col2, col3, col4 = st.columns(4)  

            col1.metric(
                "Rows",
                df.shape[0]
            )

            col2.metric(
                "Columns",
                df.shape[1]
            )

            col3.metric(
                "Missing Values",
                int(df.isnull().sum().sum())
            )
            col4.metric(
                "Duplicate Rows",
                int(df.duplicated().sum())
            )
            st.subheader("Search Dataset")

            search_term = st.text_input(
                "Search value"
            )

            if search_term:

                search_results = filtered_df[
                    filtered_df.astype(str)
                    .apply(
                        lambda row:
                        row.str.contains(
                            search_term,
                            case=False
                        ).any(),
                        axis=1
                    )
                ]

                st.write(
                    f"Found {len(search_results)} matching rows"
                )

                st.dataframe(
                    search_results,
                    use_container_width=True
                )

            st.subheader("Dataset Information")

            st.write(df.dtypes)

            st.subheader("Missing Values")

            st.write(df.isnull().sum())
            if st.button(
                "Generate Data Quality Report"
            ):

                st.subheader(
                    "Data Quality Report"
                )

                st.write(
                    "Missing Values Per Column"
                )

                st.write(
                    df.isnull().sum()
                )

                st.write(
                    "Duplicate Rows"
                )

                st.write(
                    df.duplicated().sum()
                )

            st.subheader("Available Columns")

            st.write(df.columns.tolist())

            if st.button("Generate Dataset Summary"):

                st.subheader("Statistical Summary")

                st.write(df.describe())

            csv = df.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                "⬇ Download Dataset",
                csv,
                "dataset.csv",
                "text/csv"
            )

        # =====================================================
        # VISUALIZATION TAB
        # =====================================================

        with tab2:

            st.subheader("Generate Visualization")

            x_col = st.selectbox(
                "Select X-axis Column",
                df.columns,
                key="x_axis"
            )

            y_col = st.selectbox(
                "Select Y-axis Column",
                df.columns,
                key="y_axis"
            )

            chart_type = st.selectbox(
                "Select Chart Type",
                ["Line", "Bar", "Scatter"]
            )

            if st.button(
                "Generate Chart"
            ):

                with st.spinner(
                    "Generating chart..."
                ):

                    fig = generate_chart(
                        df,
                        x_col,
                        y_col,
                        chart_type
                    )

                st.success(
                    "Chart generated successfully!"
                )

                st.pyplot(fig)

        # =====================================================
        # AI ASSISTANT TAB
        # =====================================================

        with tab3:

            st.subheader(
                "🤖 AI Data Analyst"
            )

            st.write(
                """
                Ask questions about your dataset.

                Examples:
                - What is the average revenue?
                - Show total sales.
                - Which category has the highest value?
                - Which column has missing values?
                """
            )

            user_query = st.text_input(
                "Enter your question"
            )

            if st.button(
                "Analyze Query"
            ):

                if user_query.strip():

                    with st.spinner(
                        "Analyzing dataset..."
                    ):

                        response = process_query(
                            user_query
                        )

                    st.session_state.query_history.append(
                        user_query
                    )

                    st.success(
                        response
                    )

                else:

                    st.warning(
                        "Please enter a question."
                    )

            # Query History

            if st.session_state.query_history:

                st.subheader(
                    "Previous Questions"
                )

                for index, query in enumerate(
                    reversed(
                        st.session_state.query_history
                    ),
                    start=1
                ):

                    st.write(
                        f"{index}. {query}"
                    )
            
            if st.button(
                "Clear History"
            ):

                st.session_state.query_history = []

                st.success(
                    "History Cleared Successfully"
                )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )