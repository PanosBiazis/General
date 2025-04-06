import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import plotly.graph_objects as go
import time
import mysql.connector

# Connect to MySQL database
def connect_to_database():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'aipy'
    }
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS model_data (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        feature1 FLOAT,
                        feature2 FLOAT,
                        feature3 FLOAT,
                        accuracy FLOAT)''')

def insert_data(cursor, conn, feature1, feature2, feature3, accuracy):
    cursor.execute("INSERT INTO model_data (feature1, feature2, feature3, accuracy) VALUES (%s, %s, %s, %s)",
                   (feature1, feature2, feature3, accuracy))
    conn.commit()

def fetch_data(cursor):
    cursor.execute("SELECT feature1, feature2, feature3, accuracy FROM model_data")
    data = cursor.fetchall()
    return data

# Generate sample data
data = pd.DataFrame({
    'feature1': np.random.randn(100),
    'feature2': np.random.randn(100),
    'feature3': np.random.randn(100),
    'target': np.random.randint(0, 2, 100)
})

X = data[['feature1', 'feature2', 'feature3']]
y = data['target']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Connect to MySQL database
conn, cursor = connect_to_database()
# Create table if not exists
create_table(cursor)

# Fetch data from MySQL database
data_from_db = fetch_data(cursor)

# Prepare data for plotting
x = [row[0] for row in data_from_db]
y = [row[1] for row in data_from_db]
z = [row[2] for row in data_from_db]
color = [row[3] for row in data_from_db]

# Plot 3D scatter plot with data from database using Plotly
fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=5,
        color=color,
        colorscale='Viridis',
        opacity=0.8
    )
)])

fig.update_layout(scene=dict(
                    xaxis_title='Feature 1',
                    yaxis_title='Feature 2',
                    zaxis_title='Feature 3',#),
                    bgcolor='rgba(200, 200, 230, 0.6)'),  # Background color
                    title='3D Scatter Plot of Model Data')

fig.show()

# Close database connection
cursor.close()
conn.close()
