import streamlit as st
import pandas as pd
import os

from utils.file_handler import save_uploaded_file
from utils.data_preview import load_csv
from utils.visualization import generate_chart

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

    .stButton>button {
        background-color: #4F46E5;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        border: none;
    }

    .stDownloadButton>button {
        background-color: #10B981;
        color: white;
        border-radius: 10px;
        border: none;
    }

    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border: 1px solid #e6e6e6;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
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

# ---------------- MAIN TITLE ---------------- #

st.title("StatBot Pro")

st.subheader(
    "Autonomous CSV Data Analyst"
)

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# ---------------- MAIN PROCESS ---------------- #

if uploaded_file is not None:

    try:

        # Save uploaded file
        file_path = save_uploaded_file(uploaded_file)

        st.success("File uploaded successfully!")

        # Load CSV
        df = load_csv(file_path)

        # ---------------- PREVIEW ---------------- #

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        # ---------------- METRICS ---------------- #

        col1, col2, col3 = st.columns(3)

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

        # ---------------- SUMMARY ---------------- #

        if st.button("Generate Dataset Summary"):

            st.subheader("Statistical Summary")

            st.write(df.describe())

        # ---------------- DATA TYPES ---------------- #

        st.subheader("Dataset Information")

        st.write(df.dtypes)

        # ---------------- MISSING VALUES ---------------- #

        st.subheader("Missing Values")

        st.write(df.isnull().sum())

        # ---------------- AVAILABLE COLUMNS ---------------- #

        st.subheader("Available Columns")

        st.write(df.columns.tolist())

        # ---------------- DYNAMIC VISUALIZATION ---------------- #

        st.subheader("Generate Visualization")

        x_col = st.selectbox(
            "Select X-axis Column",
            df.columns
        )

        y_col = st.selectbox(
            "Select Y-axis Column",
            df.columns
        )

        chart_type = st.selectbox(
            "Select Chart Type",
            ["Line", "Bar", "Scatter"]
        )

        if st.button("Generate Chart"):

            st.write("Generating chart...")

            chart_path = generate_chart(
                df,
                x_col,
                y_col,
                chart_type
            )

            st.success("Chart generated successfully!")

            st.image(chart_path)

        # ---------------- DOWNLOAD BUTTON ---------------- #

        csv = df.to_csv(
            index=False
        ).encode('utf-8')

        st.download_button(
            "⬇ Download Dataset",
            csv,
            "cleaned_dataset.csv",
            "text/csv"
        )

        # ---------------- AI QUERY SECTION ---------------- #

        st.subheader("Ask Questions About Dataset")

        user_query = st.text_input(
            "Example: Show highest sales region"
        )

        if st.button("Analyze Query"):

            query = user_query.lower()

            if "highest" in query or "max" in query:

                st.success(
                    "Detected operation: Maximum Value Analysis"
                )

            elif "average" in query or "mean" in query:

                st.success(
                    "Detected operation: Average Calculation"
                )

            elif "total" in query or "sum" in query:

                st.success(
                    "Detected operation: Sum Aggregation"
                )

            else:

                st.info(
                    "AI Query Engine Integration Coming Soon..."
                )

    except Exception as e:

        st.error(f"Error: {e}")