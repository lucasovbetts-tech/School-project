from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/Contact')
def contact():
    return render_template('contact.html')

@app.route('/JS/RenderHeader.js')
def render_header_script():
    return send_from_directory(app.root_path + '/JS', 'RenderHeader.js')

app.run(debug=True)