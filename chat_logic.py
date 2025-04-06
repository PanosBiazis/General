# # chat_logic.py
# import sqlite3
# import sys

# def get_response(user_input):
#     conn = sqlite3.connect(r'C:\xampp\htdocs\chatbot\chatbot.db')
#     cursor = conn.cursor()

#     # Basic query to fetch a predefined response
#     cursor.execute("SELECT response FROM responses WHERE question = ?", (user_input,))
#     result = cursor.fetchone()
    
#     conn.close()

#     if result:
#         return result[0]
#     else:
#         return "I'm not sure how to respond to that."

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         user_input = sys.argv[1]
#         print(get_response(user_input))
#     else:
#         print("No input provided")


import sqlite3
import sys
import os

# Path to the SQLite database file
db_path = 'C:\\xampp\\htdocs\\chatbot\\chatbot.db'

# Function to create the 'responses' table if it doesn't exist
def create_table_if_not_exists():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the 'responses' table and insert sample data if not present
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT UNIQUE,
        response TEXT
    );

    INSERT OR IGNORE INTO responses (question, response) VALUES ('Hello', 'Hi there! How can I help you?');
    INSERT OR IGNORE INTO responses (question, response) VALUES ('How are you?', 'I am just a program, but I am functioning as expected.');
    ''')

    conn.commit()
    conn.close()

# Function to get a response from the database
def get_response(user_input):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to fetch the response
        cursor.execute("SELECT response FROM responses WHERE question = ?", (user_input,))
        result = cursor.fetchone()

        conn.close()

        # Return the response or a default message if no match is found
        return result[0] if result else "I'm not sure how to respond to that."

    except sqlite3.Error as e:
        return f"Database error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Main script execution
if __name__ == "__main__":
    # Create the table if not exists before proceeding
    create_table_if_not_exists()

    # Check if an argument is provided for the user input
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        response = get_response(user_input)
        print(response)
    else:
        print("No input provided")
