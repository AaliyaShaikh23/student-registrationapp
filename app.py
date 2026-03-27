from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    phone = request.form.get('phone', '').strip()
    course = request.form.get('course', '').strip()
    address = request.form.get('address', '').strip()

    if not all([name, email, phone, course, address]):
        return render_template('message.html', message="All fields are required.")

    if not phone.isdigit() or len(phone) != 10:
        return render_template('message.html', message="Phone number must be 10 digits.")

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO students (name, email, phone, course, address)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (name, email, phone, course, address)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return render_template('message.html', message="Student registered successfully!")

    except mysql.connector.IntegrityError:
        return render_template('message.html', message="Email already exists. Try another email.")

    except Error as e:
        return render_template('message.html', message=f"Database error: {e}")

@app.route('/students')
def students():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM students ORDER BY id DESC")
        students_data = cursor.fetchall()

        cursor.close()
        connection.close()

        return render_template('students.html', students=students_data)

    except Error as e:
        return render_template('message.html', message=f"Database error: {e}")

if __name__ == '__main__':
    app.run(debug=True)