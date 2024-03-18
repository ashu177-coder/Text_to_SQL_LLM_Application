# Application for converting text to sql queries and giving the result set as a response to the user's question for data

# Agenda -> Text To SQL LLM Application
# Prompt -> LLM(Gemini Pro) -> SQL Query -> Database -> Response

# Implementation
# 1.SQLite -> Insert some records(through python database connection)
# 2.LLM Application -> Gemini Pro -> SQL Database
import sqlite3

# Connecting to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor
cursor = connection.cursor()

# Create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), 
SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

# Inserting records in the database
cursor.execute("""
               Insert into STUDENT VALUES ('Krish', 'Data Science', 'A', 90), ('Sudhanshu', 'Data Science', 'B', 100), ('Darius', 'Data Science', 'A', 86), ('Vikas', 'DevOPS', 'A', 50), ('Dipesh', 'DevOPS', 'A', 35);
               """)

# Display all the records
print("The Inserted records are: ")
data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

# Closing the connection
connection.commit()
connection.close()
