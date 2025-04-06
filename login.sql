-- Create the database
CREATE DATABASE fashion_store;

-- Use the database
USE fashion_store;

-- Create the users table
CREATE TABLE users (
    user_id INT(6) AUTO_INCREMENT PRIMARY KEY,  -- Unique ID for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Username must be unique
    pwd VARCHAR(255) NOT NULL,            -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,        -- Email must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);
