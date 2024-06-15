from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welco   me to the seat reservation website!'

@app.route('/reservation')
def reservation():
    return 'This is the reservation page.'

@app.route('/reserve', methods=['POST'])
def reserve():
    name = request.form['name']
    event = request.form['event']
    seats = request.form
