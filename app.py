# imports
from flask import Flask

#create app
app = Flask(__name__)

#create root
@app.route('/')
def hello_world():
    return 'Hello world'
