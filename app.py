import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database setup: Connect to SQLite and create users table if it doesn't exist
def init_db():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL)''')
    connection.commit()
    connection.close()

# Run the init_db function to ensure the database is set up
init_db()

# Route for login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Insert the new user into the database
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connection.commit()
        cursor.close()
        connection.close()

        return f"User '{username}' added successfully to the database!"

    return render_template('index.html')

# Route to view all users stored in the database
@app.route('/view_users')
def view_users():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('view_users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
