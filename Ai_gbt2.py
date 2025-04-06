from flask import Flask, render_template
import mysql.connector

app = Flask(__name__,template_folder=r"")#pathfile

# Connect to MySQL database
def connect_to_database():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'ai_gbt'
    }
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    return conn, cursor

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table')
def table():
    conn, cursor = connect_to_database()
    cursor.execute("SELECT feature1, feature2, feature3, accuracy FROM model_data")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('table.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
