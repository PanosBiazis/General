import mysql.connector
import random

# Connect to the MySQL database using XAMPP
conn = mysql.connector.connect(
    host='localhost',
    user='root',         # Default XAMPP user; change if you have a different user
    password='',         # Default is empty; change if you set a root password
    database='ai_gbt'    # Name of your database
)

cursor = conn.cursor()

# Function to insert random accuracy values
def insert_random_accuracy(num_records):
    for _ in range(num_records):
        # Generate random values for the features and accuracy
        feature1 = random.uniform(0, 100)  # Adjust range as needed
        feature2 = random.uniform(0, 100)
        feature3 = random.uniform(0, 100)
        accuracy = random.uniform(0, 1)    # Assuming accuracy is between 0 and 1

        # Insert the generated data into the table
        cursor.execute('''
            INSERT INTO model_data (feature1, feature2, feature3, accuracy)
            VALUES (%s, %s, %s, %s)
        ''', (feature1, feature2, feature3, accuracy))

    # Commit the changes
    conn.commit()

print("How many data do you want to insert?")
num_records = int(input("Number of Data: "))

# Insert 10 random records (adjust as needed)
insert_random_accuracy(num_records)

# Close the connection
cursor.close()
conn.close()

print("Random data inserted successfully.")
