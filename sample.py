from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',         # replace with your MySQL username
    'password': 'Babulal007$', # replace with your MySQL password
    'database': 'flask_app'
}

@app.route("/")
def home():
    return render_template("index.html")  # your form page

@app.route("/submit", methods=['POST'])
def submit():
    
    # Get form data
    fn = request.form.get('first_name')
    ln = request.form.get('last_name')
    age = request.form.get('age')
    ph_no = request.form.get('phone_number')

    # Print for debug
    print(f"{fn} {ln}, age {age}, phone {ph_no}")

    try:
        # Connect to MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert data
        sql = "INSERT INTO person_data (first_name, last_name, age, phone_number) VALUES (%s, %s, %s, %s)"
        data = (fn, ln, age, ph_no)
        cursor.execute(sql, data)
        connection.commit()

        cursor.close()
        connection.close()

        return render_template("submitted.html")  # success page

    except mysql.connector.Error as err:
        print("Error:", err)
        return f"Database error: {err}"

@app.route("/submitted")
def submitted():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
