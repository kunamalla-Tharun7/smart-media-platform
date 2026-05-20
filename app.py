import streamlit as st

from db_c import db_connection,cur_obj
st.title("Media Platform")
tab1,tab2=st.tabs(
[
    "Login","Signup"
])

with tab1:
    st.header("Login")
    with st.form("Login_form"):
        emaill=st.text_input("Email ")
        passwordl=st.text_input("Password",type="password")
        btn1=st.form_submit_button("Login")
        if btn1:
            query="select * from users where email=%s and password=%s"
            data=(emaill,passwordl)
            cur_obj.execute(query,data)
            db_connection.commit()
            st.success("Login Successful ✔️..")


with tab2:
    st.header("Signup")
    with st.form("Signup_form"):
        name=st.text_input("Name")
        email=st.text_input("Email")
        password=st.text_input("password")
        confirm_password=st.text_input("confirm password")
        btn2=st.form_submit_button("Signup")
         

        if btn2:
            query=" insert into users(name,email,password) values(%s,%s,%s)"
            data=(name,email,password)
            cur_obj.execute(query,data)
            db_connection.commit()
            st.success("Signup Successful ✔️...")