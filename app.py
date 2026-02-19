from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! <br> Welcome to Version 1 Digital Skills Academy'
