from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__.split('.')[0])
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'normies'
# setup context
app.app_context()
# initialize db
db.init_app(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(80),nullable=False)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
# @app.route('/userstatic')
# def user():
#     return {
#         "name":"teguh",
#         "age":25,
#         "hobbies":["eat","sleep","learning"]
#     }

    

if __name__ == '__main__':
    app.run(debug=True)