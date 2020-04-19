from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key" # Deze key wordt gebruikt om wachtwoorden te salten.


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud' # protocol://gebruikersnaam:wachtwoord@host/database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
