# import sqlite3

# # Path to the database
# db_path = 'C:\\xampp\\htdocs\\chatbot\\chatbot.db'

# # Connect to the database (it will create if not exists)
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# # Create the 'responses' table
# cursor.executescript('''
# CREATE TABLE IF NOT EXISTS responses (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     question TEXT UNIQUE,
#     response TEXT
# );

# INSERT OR IGNORE INTO responses (question, response) VALUES ('Hello', 'Hi there! How can I help you?');
# INSERT OR IGNORE INTO responses (question, response) VALUES ('How are you?', 'I am just a program, but I am functioning as expected.');
# ''')

# conn.commit()
# conn.close()

# # print("Database and table created successfully.")

# import sqlite3

# # Path to the database
# db_path = 'C:\\xampp\\htdocs\\chatbot\\chatbot.db'

# # Connect to the database (it will create if not exists)
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# # Create the 'responses' table
# cursor.executescript('''
# CREATE TABLE IF NOT EXISTS responses (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     question TEXT UNIQUE,
#     response TEXT
# );

# INSERT OR IGNORE INTO responses (question, response) VALUES ('Hello', 'Hi there! How can I help you?');
# INSERT OR IGNORE INTO responses (question, response) VALUES ('How are you?', 'I am just a program, but I am functioning as expected.');
# ''')

# conn.commit()
# conn.close()

# print("Database and table created successfully.")


import sqlite3

# Path to the database
db_path = 'C:\\xampp\\htdocs\\chatbot\\chatbot.db'

# Connect to the database (it will create if not exists)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the 'responses' table
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

print("Database and table created successfully.")
