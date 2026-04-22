from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "mysql"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", "root"),
        database=os.environ.get("MYSQL_DB", "test")
    )

@app.route("/")
def home():
    return "Flask + MySQL API running 🚀"

@app.route("/messages", methods=["GET"])
def get_messages():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages")
    data = cursor.fetchall()
    conn.close()

    return jsonify(data)

@app.route("/add", methods=["POST"])
def add_message():
    data = request.get_json()
    message = data.get("message")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
    conn.commit()
    conn.close()

    return {"status": "message added"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
