import google.generativeai as genai
import sqlite3
import os
import streamlit as st
from dotenv import load_dotenv

# Loading the environment variables
load_dotenv()

# Configuring the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the gemini pro model and provide the SQL query as reponse
# Prompt is how I want the LLM Model to behave


def get_gemini_response(prompt, question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

# Hitting the returned SQL query to the database and returning the response


def read_sql_query(query, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows


# Defining the prompt and the streamlit page
prompt = """
You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS\n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
"""

st.set_page_config(page_title="NLP to SQL")
st.header("Gemini App to retrieve SQL data")

question = st.text_input("Input: ", key='input')
submit = st.button("Ask the question:")

# if submit is clicked
if submit:
    sql_query = get_gemini_response(prompt, question)
    print(f"The SQL query corresponding to the question is -> {sql_query}")
    data = read_sql_query(sql_query, "student.db")
    st.subheader("The Response is -> ")
    for row in data:
        print(row)
        st.write(row)
