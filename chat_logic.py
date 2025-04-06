# # chat_logic.py
# import sqlite3
# import sys

# def get_response(user_input):
#     conn = sqlite3.connect('chatbot.db')
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

def get_response(user_input):
    try:
        conn = sqlite3.connect('chatbot.db')
        cursor = conn.cursor()
        cursor.execute("SELECT response FROM responses WHERE question = ?", (user_input,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "I'm not sure how to respond to that."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        print(get_response(user_input))
    else:
        print("No input provided")
