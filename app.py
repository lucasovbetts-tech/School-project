from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/Home')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/About')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Contact')
@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(debug=True)