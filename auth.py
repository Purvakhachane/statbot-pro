import streamlit as st


def initialize_auth():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "users" not in st.session_state:
        st.session_state.users = {
            "admin": "admin123"
        }

    if "username" not in st.session_state:
        st.session_state.username = ""


def show_auth():

    initialize_auth()

    st.title("📊 StatBot Pro")

    st.subheader(
        "Please Login or Create an Account"
    )

    login_tab, signup_tab = st.tabs(
        ["🔐 Login", "📝 Signup"]
    )

    # ---------------- LOGIN ---------------- #

    with login_tab:

        st.subheader("Login")

        username = st.text_input(
            "Username",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Login"
        ):

            users = st.session_state.users

            if (
                username in users
                and users[username] == password
            ):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success(
                    "Login Successful"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid Username or Password"
                )

    # ---------------- SIGNUP ---------------- #

    with signup_tab:

        st.subheader(
            "Create Account"
        )

        new_username = st.text_input(
            "Username",
            key="signup_username"
        )

        new_password = st.text_input(
            "Password",
            type="password",
            key="signup_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            key="confirm_password"
        )

        if st.button(
            "Create Account"
        ):

            if not new_username.strip():

                st.error(
                    "Username cannot be empty"
                )

            elif new_password != confirm_password:

                st.error(
                    "Passwords do not match"
                )

            elif new_username in st.session_state.users:

                st.error(
                    "Username already exists"
                )

            else:

                st.session_state.users[
                    new_username
                ] = new_password

                st.success(
                    "Account Created Successfully"
                )

                st.info(
                    "Now login using your new account."
                )