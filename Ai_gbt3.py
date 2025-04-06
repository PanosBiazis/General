
# import random
# import keyboard
# import mysql.connector
# import time

# # Database connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ai_gbt"
# )
# cursor = db.cursor()

# print("Generating random numbers. Press ESC or Ctrl+C to stop...")

# try:
#     while True:
#         # Generate random number
#         random_number = random.randint(1, 1000)
        
#         # Insert into database
#         sql = "INSERT INTO random_numbers (number) VALUES (%s)"
#         cursor.execute(sql, (random_number,))
#         db.commit()
        
#         print(f"Generated and inserted: {random_number}")
        
#         # Check if ESC is pressed
#         if keyboard.is_pressed('esc'):
#             print("\nESC pressed. Stopping...")
#             break
            
#         time.sleep(1)  # Wait 1 second before next number

# except KeyboardInterrupt:
#     print("\nCtrl+C pressed. Stopping...")

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     cursor.close()
#     db.close()
#     print("Database connection closed.")
import random
import keyboard
import mysql.connector
import time

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ai_gbt"
)
cursor = db.cursor()

print("Generating random model data. Press ESC or Ctrl+C to stop...")

try:
    while True:
        # Generate random values for each column
        feature1 = random.uniform(0, 100000)  # Random float between 0 and 10
        feature2 = random.uniform(0, 100000)
        feature3 = random.uniform(0, 100000)
        accuracy = random.uniform(0.0000, 1.0000)  # Random accuracy between 70% and 100%
        
        # Insert into database
        sql = "INSERT INTO model_data (feature1, feature2, feature3, accuracy) VALUES (%s, %s, %s, %s)"
        values = (feature1, feature2, feature3, accuracy)
        cursor.execute(sql, values)
        db.commit()
        
        print(f"Generated and inserted: Feature1={feature1:.10f}, Feature2={feature2:.10f}, Feature3={feature3:.10f}, Accuracy={accuracy:.10f}")
        
        # Check if ESC is pressed
        if keyboard.is_pressed('esc'):
            print("\nESC pressed. Stopping...")
            break
            
        time.sleep(1)  # Wait 1 second before next data point

except KeyboardInterrupt:
    print("\nCtrl+C pressed. Stopping...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    cursor.close()
    db.close()
    print("Database connection closed.")
