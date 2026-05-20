import mysql.connector 
import streamlit as st 

db_connection=mysql.connector.connect(
    host=st.secrets["Host_Name"],
    user=st.secrets["user"],
    database=st.secrets["database"],
    password=st.secrets["password"],
    port=st.secrets["port"]
)

cur_obj=db_connection.cursor(dictionary=True)

cur_obj.execute("""
                CREATE TABLE IF NOT EXISTS users(
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(50) NOT NULL,
                email VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL)
                """
)

cur_obj.execute("""
                 CREATE TABLE IF NOT EXISTS files(
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT,
                file_name VARCHAR(255),
                file_type VARCHAR(100),
                file_url TEXT,
                upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
                
                )
                
                """)
db_connection.commit()
