-- chatbot_db.sql
CREATE TABLE responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT UNIQUE,
    response TEXT
);

-- Insert sample data
INSERT INTO responses (question, response) VALUES ('Hello', 'Hi there! How can I help you?');
INSERT INTO responses (question, response) VALUES ('How are you?', 'I am just a program, but I am functioning as expected.');
