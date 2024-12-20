from flask import Flask , render_template 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mydatabase.sqlite3"

db = SQLAlchemy(app)

app.app_context().push()

# ========== Model for ONE to MANY RELATIONSHIP ===============

# Child Table 
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),nullable = False,unique = True)
    password = db.Column(db.String(),nullable = False)
    # role_id = db.Column(db.Integer, db.Foreign_key('role.id'))

# Parent Table
class Role(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    rolename = db.Column(db.String(),nullable = False, unique = True)
    # users = db.Relationship('User',backref='role')





