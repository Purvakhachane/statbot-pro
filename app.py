import streamlit as st
import pandas as pd

# ================= DEBUG IMPORT CHECK =================
import charts
print("charts loaded from:", charts.__file__)

# ================= CUSTOM MODULE IMPORTS =================
from charts import create_bar_chart, create_histogram, create_line_chart
from insights import (
    get_missing_values,
    get_dataset_shape,
    get_correlation,
    get_dataset_summary,
    get_numeric_insights
)

# ================= PAGE CONFIG =================
st.set_page_config(page_title="StatBot Pro", layout="wide")

st.title("📊 StatBot Pro - Smart Visualization Dashboard")

# ================= FILE UPLOAD =================
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        # ================= DATA PREVIEW =================
        st.subheader("📄 Dataset Preview")
        st.dataframe(df)

        # ================= KPI SECTION =================
        st.subheader("📊 KPI Dashboard")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Missing Values", df.isnull().sum().sum())
        col4.metric("Numeric Columns", len(df.select_dtypes(include="number").columns))

        # ================= VISUALIZATION =================
        st.subheader("📈 Visualization Module")

        chart_type = st.selectbox(
            "Select Chart Type",
            ["Histogram", "Bar Chart", "Line Chart"]
        )

        columns = df.columns.tolist()

        col_x = st.selectbox("Select X-axis / Column", columns)

        col_y = None
        if chart_type != "Histogram":
            col_y = st.selectbox("Select Y-axis Column", columns)

        # ================= GENERATE CHART =================
        if chart_type == "Histogram":
            fig = create_histogram(df, col_x)
            st.pyplot(fig)

        elif chart_type == "Bar Chart":
            fig = create_bar_chart(df, col_x, col_y)
            st.pyplot(fig)

        elif chart_type == "Line Chart":
            fig = create_line_chart(df, col_x, col_y)
            st.pyplot(fig)

        # ================= INSIGHTS (OPTIONAL FEATURE) =================
        st.subheader("🧠 Auto Insights")

        try:
            insights = generate_insights(df)
            st.write(insights)
        except Exception as e:
            st.warning(f"Insights module error: {e}")

    except Exception as e:
        st.error(f"Error reading file: {e}")

else:
    st.info("⬆ Upload a CSV file to start analysis")