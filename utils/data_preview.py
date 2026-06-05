import streamlit as st
import pandas as pd

@st.cache_data
def load_csv(file_path):
    return pd.read_csv(file_path)