import streamlit as st

from utils.file_handler import save_uploaded_file
from utils.data_preview import load_csv

st.title("StatBot Pro - Dataset Preview")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        # Save file
        file_path = save_uploaded_file(uploaded_file)

        st.success("File uploaded successfully!")

        # Load CSV
        df = load_csv(file_path)

        st.subheader("Dataset Preview")

        # Show first 5 rows
        st.dataframe(df.head())

        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

    except Exception as e:
        st.error(f"Error: {e}")