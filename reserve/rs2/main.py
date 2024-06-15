from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('seats.db')
    c = conn.cursor()
    c.execute("SELECT * FROM seats")
    seats = c.fetchall()
    conn.close()
    return render_template('index.html', seats=seats)

@app.route('/reserve', methods=['POST'])
def reserve():
    seat_number = request.form['seat']
    conn = sqlite3.connect('seats.db')
    c = conn.cursor()
    c.execute("UPDATE seats SET status='reserved' WHERE number=?", (seat_number,))
    conn.commit()
    conn.close()
    return "Reservation successful!"
    
if __name__ == '__main__':
    app.run(debug=True)
