# SQL-QUERY-GENERATOR
This project is a Streamlit app that converts natural language questions into SQL queries using Google’s Gemini AI model and executes them on a PostgreSQL database. Users can input questions, view the generated SQL query, and see the query results—all in one interactive interface.

# README
# SQL Query Generator and Executor with Google Generative AI
This project provides a simple web application to translate natural language questions into SQL queries, which are then executed on a PostgreSQL database. The application leverages Google Generative AI's Gemini model for NLP-to-SQL transformation and displays the results in a Streamlit interface.

Table of Contents
Features
Setup
Running the App
Example Use Case
Project Structure
Environment Variables
Dependencies
Features
Convert natural language questions into SQL queries.
Run generated SQL queries against a PostgreSQL database.
Display query results in a simple and interactive UI.
Setup
Prerequisites
Python: Ensure Python 3.x is installed on your system.

PostgreSQL Database: Make sure PostgreSQL is installed and running. Create a database named Customer_details and a table named user_activities with columns as specified.

Google Generative AI: Obtain an API key from Google Cloud for accessing the Gemini model.

Install Dependencies
Clone the repository.
Create a virtual environment and activate it:
bash
Copy code
python -m venv env
source env/bin/activate  # For macOS/Linux
.\env\Scripts\Activate   # For Windows
Install the dependencies:
bash
Copy code
pip install -r requirements.txt
Environment Variables
Create a .env file in the root directory.
Add the following environment variables:
plaintext
Copy code
GOOGLE_API_KEY=your_google_api_key
PG_PASSWORD=your_postgresql_password
Note: Replace your_google_api_key and your_postgresql_password with the actual values.
Running the App
Activate the virtual environment (if not already activated).

Run the Streamlit app with:

bash
Copy code
streamlit run app_gemini.py
The app should open in a web browser at http://localhost:8501.

Example Use Case
Input a Question: Type a question in natural language about the data in your user_activities table. Example: "Show all activities where status is completed."
Generate and Execute SQL: Click on Ask the question to generate and execute the query.
View Results: The SQL query and its results are displayed on the page.
Project Structure
plaintext
Copy code
.
├── app_gemini.py          # Main Streamlit application
├── requirements.txt       # Python package dependencies
├── .env                   # Environment variables (not included in repo)
└── README.md              # This README file
Environment Variables
GOOGLE_API_KEY: API key for Google Generative AI.
PG_PASSWORD: Password for connecting to your PostgreSQL database.
Dependencies
google-generativeai: Library for interacting with Google Generative AI.
pg8000: A PostgreSQL driver for Python.
streamlit: Framework for building interactive web applications.
