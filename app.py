from flask import Flask, render_template, jsonify
import sqlite3
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)

DATABASE = 'employee.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM employee_data"
    cursor.execute(query)

    data = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
