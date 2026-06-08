import streamlit as st

from auth import show_auth
from main_dashboard import show_dashboard

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="StatBot Pro",
    layout="wide"
)

# ---------------- SESSION STATE ---------------- #

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {
        "admin": "admin123"
    }

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- ROUTER ---------------- #

if st.session_state.logged_in:

    show_dashboard()

else:

    show_auth()