from flask import render_template
from app import app


# Define the first view
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Home')


@app.route('/maps/')
def maps():
    return render_template('lived_map.html', title='Maps',
                           map_type='mapbox.streets')


@app.route('/blog/')
def blog():
    return render_template('blog.html', title='Blog')
