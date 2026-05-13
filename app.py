import streamlit as st
import pandas as pd
import os

st.title("StatBot Pro - Dataset Preview")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    try:
        df = pd.read_csv(file_path)

        st.subheader("Dataset Preview")

        st.dataframe(df.head())

        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

    except Exception as e:
        st.error(f"Error reading file: {e}")