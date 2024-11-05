import os
import google.generativeai as genai
import streamlit as st
import pg8000
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API key for Google Generative AI
genai.configure(api_key="YOUR GEMINI API KEY HERE") 

# Function to load google-gemini model and provide SQL query as a response
def get_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])

    # Clean up the SQL query by removing unwanted parts
    cleaned_query = response.text.strip()

    # Remove prefixes like "SQL Query:"
    if "SQL Query:" in cleaned_query:
        cleaned_query = cleaned_query.split("SQL Query:")[-1].strip()

    # Remove any code block indicators or unwanted characters
    cleaned_query = cleaned_query.replace("```sql", "").replace("```", "").strip()

    # Ensure no numbered lists or bullet points are included
    cleaned_query = cleaned_query.lstrip("0123456789.- ")  # remove leading numbers, bullets, etc.

    return cleaned_query

# Function to execute SQL query and retrieve data from PostgreSQL database
def read_sql_query(sql):
    try:
        # Connect to PostgreSQL database
        con = pg8000.connect(
            database='Customer_details',
            user='postgres',
            password='root',  # Use environment variable for password
            host='localhost',
            port=5433
        )
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        con.commit()
        return rows
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        con.close()

# Define the prompt for the generative AI model
prompt = """
You are an expert in SQL and understand database schemas. I have a PostgreSQL database. Here are the details:

- Table: `user_activities`
  - Columns: `activity_id`, `user_id`, `username`, 'activity_type', 'activity_description', 'activity_date', 'duration', 'status'

Convert the following natural language question into a single SQL query:
"""

# Streamlit app
st.set_page_config(page_title="SQL QUERY RETRIEVER")
st.header("SQL QUERY GENERATOR")

Question = st.text_input("Input: ", key="Input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    sql_query = get_response(Question, prompt)
    st.subheader("Generated SQL Query:")
    st.code(sql_query, language='sql')

    try:
        data = read_sql_query(sql_query)
        st.subheader("Query Results:")
        if data:
            for row in data:
                st.write(row)
        else:
            st.write("No results found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
