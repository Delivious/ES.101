from flask import Flask, request, jsonify, render_template, redirect, url_for
import datetime
import sqlite3
import threading
import time
app = Flask(__name__)
app.secret_key = 'your_secret_key'


def init_db():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
def dbConnection():
    conn = sqlite3.connect('logs.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def home():
    with dbConnection() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM logs")
        rows = c.fetchall()
        return render_template('logs.html', data=rows)

@app.route('/api/logs', methods=['GET', 'POST'])
def get_logs():
    if request.method == 'POST':
        print('Motion detected')
        current_time = datetime.datetime.now().strftime("%m/%d/%Y - %H:%M:%S")
        with dbConnection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO logs (time) VALUES (?)", (current_time,))
            threading.Timer(100, delete_log, args=(c.lastrowid,)).start()
        return 200

def delete_log(log_id):
    with dbConnection() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM logs WHERE id = ?", (log_id,))
    return 200
def delete_old_logs():
    with sqlite3.connect('logs.db') as conn:
        c = conn.cursor()
        c.execute("DELETE FROM logs WHERE time < datetime('now', '-5 minutes')")
        conn.commit()

@app.route('/api/returnLogs', methods=['GET'])
def return_logs():
    with dbConnection() as conn:
        c = conn.cursor()
        rows = c.execute("SELECT * FROM logs").fetchall()
        x = 0
        for row in rows:
            x+=1
            
        return {"count": x}

init_db()
app.run(debug=True, host='0.0.0.0', port=5000)
