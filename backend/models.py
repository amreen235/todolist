from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    
    username = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    tasks = db.relationship("Task", backref="user", lazy=True)


class Login(db.Model):
    __tablename__ = "login"

    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    isLoggedIn = db.Column(db.Boolean, default=False)


class Task(db.Model):
    __tablename__ = "tasks"

    tid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    username = db.Column(db.String(80), db.ForeignKey("users.username"), nullable=False)
