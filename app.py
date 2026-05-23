import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

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

    # Create uploads folder
    os.makedirs("uploads", exist_ok=True)

    # Save file
    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    try:

        # Read CSV
        df = pd.read_csv(file_path)

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

        # ---------------- SUMMARY BUTTON ---------------- #

        if st.button("Generate Dataset Summary"):

            st.subheader("Statistical Summary")

            st.write(df.describe())

        # ---------------- DATA TYPES ---------------- #

        st.subheader("Dataset Information")

        st.write(df.dtypes)

        # ---------------- MISSING VALUES ---------------- #

        st.subheader("Missing Values")

        st.write(df.isnull().sum())

        # ---------------- VISUALIZATION ---------------- #

        numeric_cols = df.select_dtypes(
            include='number'
        ).columns

        if len(numeric_cols) >= 2:

            st.subheader("Interactive Visualization")

            x_axis = st.selectbox(
                "Select X-Axis",
                numeric_cols
            )

            y_axis = st.selectbox(
                "Select Y-Axis",
                numeric_cols,
                index=1
            )

            chart_type = st.radio(
                "Choose Chart Type",
                ["Bar Chart", "Line Chart"]
            )

            fig, ax = plt.subplots(figsize=(10, 5))

            if chart_type == "Bar Chart":

                df[[x_axis, y_axis]].head(10).plot(
                    kind='bar',
                    ax=ax
                )

            else:

                df[[x_axis, y_axis]].head(10).plot(
                    kind='line',
                    ax=ax
                )

            st.pyplot(fig)

        else:

            st.info(
                "Not enough numeric columns available for visualization."
            )

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

        st.error(
            f"Error reading file: {e}"
        )