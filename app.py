from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    x = 5
    return  'Hello, World! <br><br> Welcome to Version 1 Digital Skills Academy <br><br> Lets create a variable: <br><br> x =' 
            
