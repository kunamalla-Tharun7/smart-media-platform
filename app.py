import streamlit as st

st.title("Media Platform")
tab1,tab2=st.tabs(
[
    "Login","Signup"
])

with tab1:
    st.header("Login")
    with st.form("Login_form"):
        st.text_input("Email ")
        st.text_input("Password",type="password")
        btn1=st.form_submit_button("Login")
        if btn1:
            st.success("Login Successful...")

with tab2:
    st.header("Signup")
    with st.form("Signup_form"):
        st.text_input("Name")
        st.text_input("Email")
        st.text_input("password")
        st.text_input("confirm password")
        btn2=st.form_submit_button("Signup")
        if btn2:
            st.success("Signup Successful...")


