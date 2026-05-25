import streamlit as st

from utils.file_handler import save_uploaded_file
from utils.data_preview import load_csv
from utils.visualization import generate_chart

# Page title
st.title("StatBot Pro - CSV Data Analyst")

# File uploader
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# Check if file uploaded
if uploaded_file is not None:

    try:
        # Save uploaded file
        file_path = save_uploaded_file(uploaded_file)

        st.success("File uploaded successfully!")

        # Load CSV data
        df = load_csv(file_path)

        # Dataset preview section
        st.subheader("Dataset Preview")

        st.dataframe(df.head())

        # Dataset information
        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

        # Show column names
        st.subheader("Available Columns")

        st.write(df.columns.tolist())

        # Visualization section
        st.subheader("Generate Visualization")

        # X-axis selection
        x_col = st.selectbox(
            "Select X-axis Column",
            df.columns
        )

        # Y-axis selection
        y_col = st.selectbox(
            "Select Y-axis Column",
            df.columns
        )

        # Chart type selection
        chart_type = st.selectbox(
            "Select Chart Type",
            ["Line", "Bar", "Scatter"]
        )

        # Generate chart button
        if st.button("Generate Chart"):

            st.write("Generating chart...")

            chart_path = generate_chart(
                df,
                x_col,
                y_col,
                chart_type
            )

            st.success("Chart generated successfully!")

            # Display chart
            st.image(chart_path)

    except Exception as e:

        st.error(f"Error: {e}")