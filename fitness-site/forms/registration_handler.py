from flask import request, redirect, url_for, flash
from datetime import datetime
import sqlite3

def handle_registration():
    if request.method == 'POST':
        name = request.form['full_name']
        age = request.form['age']
        gender = request.form['gender']
        phone = request.form['phone_number']
        whatsapp = request.form['whatsapp_number']
        email = request.form['email']
        city = request.form['city']
        height = request.form['height']
        weight = request.form['weight']
        fitness_goal = request.form['fitness_goal']
        activity_level = request.form['activity_level']
        preferred_training = request.form['preferred_training']
        message = request.form['message']

        # Validate fields (basic example)
        if not name or not phone or not fitness_goal:
            flash('Please fill in all required fields.')
            return redirect(url_for('home'))

        # Connect to the database
        conn = sqlite3.connect('database/enquiries.db')
        cursor = conn.cursor()

        # Insert the enquiry into the database
        cursor.execute('''
            INSERT INTO Enquiries (name, age, gender, phone, email, city, height, weight, fitness_goal, activity_level, preferred_training, message, created_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, age, gender, phone, email, city, height, weight, fitness_goal, activity_level, preferred_training, message, datetime.now(), 'Pending'))

        conn.commit()
        conn.close()

        flash('Your enquiry has been submitted successfully!')
        return redirect(url_for('home'))

    return redirect(url_for('home'))  # Redirect if not a POST request