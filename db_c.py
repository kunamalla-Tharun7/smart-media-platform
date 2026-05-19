import mysql.connector 
import streamlit as st 

db_connection=mysql.connector.connect(
    host=st.secrets["Host_Name"],
    user=st.secrets["user"],
    database=st.secrets["database"],
    password=st.secrets["password"],
    port=st.secrets["port"]

db_connection= mysql.connector.connect(
    host=st.secrets["MYSQL_HOST"],
    port=st.secrets["MYSQL_PORT"],
    user=st.secrets["MYSQL_USER"],
    password=st.secrets["MYSQL_PASSWORD"],
    database=st.secrets["MYSQL_DB"]
)

cursor=conn.cursor(dictionary=True)
