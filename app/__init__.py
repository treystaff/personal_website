from flask import Flask

# Create the flask app
print(__name__)
app = Flask(__name__)
app.debug = True
from app import views
