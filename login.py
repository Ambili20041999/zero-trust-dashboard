import streamlit as st

# Login Function
def login():

    st.title("Zero Trust Dashboard Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":
            st.session_state["logged_in"] = True
            st.success("Login Successful")
        else:
            st.error("Invalid Username or Password")


# Check Login Status
def check_login():

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    return st.session_state["logged_in"]


# Logout Function
def logout():

    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()