from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database/enquiries.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['full_name']
    age = request.form['age']
    gender = request.form['gender']
    phone = request.form['phone']
    whatsapp = request.form['whatsapp']
    email = request.form['email']
    city = request.form['city']
    height = request.form['height']
    weight = request.form['weight']
    fitness_goal = request.form['fitness_goal']
    activity_level = request.form['activity_level']
    preferred_training = request.form['preferred_training']
    message = request.form['message']
    created_date = datetime.now()
    status = 'New'

    conn = get_db_connection()
    conn.execute('INSERT INTO enquiries (name, age, gender, phone, email, city, height, weight, fitness_goal, activity_level, preferred_training, message, created_date, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 (name, age, gender, phone, email, city, height, weight, fitness_goal, activity_level, preferred_training, message, created_date, status))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)