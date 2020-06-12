from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = 'f8bcff1dc840085af10535ca4673c3a5'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)


from bluethoughts import routes
