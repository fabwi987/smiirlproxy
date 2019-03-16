from flask import (
    Flask,
    render_template,
    jsonify, 
    request
)
from gevent.pywsgi import WSGIServer

CONST_MAX_VALUE = 99999
CONST_MIN_VALUE = 0
value = 0

# Create the application instance
app = Flask(__name__, template_folder="templates")

# URL route that displays the value
@app.route('/')
def home():
    global value
    number = {
        "Number": value
    }
    return jsonify(number)

# URL route for setting a value
@app.route('/set')
def se():
    global value
    incoming_value = request.args.get('value')
    if validInput(incoming_value):
        value = incoming_value
    else:
        return "Value is not within the allowed range"
    return "Value updated"  

# URL route for increasing the value by one
@app.route('/callback')
def increase():
    global value
    value = value + 1
    return "Registered"

def validInput(incoming_value):
    return int(incoming_value) < CONST_MAX_VALUE and int(incoming_value) > CONST_MIN_VALUE

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    #Debug/development
    #app.run(debug=True, host='0.0.0.0', port=5000)
    #Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()