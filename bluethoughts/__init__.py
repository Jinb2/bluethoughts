from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = 'f8bcff1dc840085af10535ca4673c3a5'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ythqzyzjmjsbmv:b6f387ce17de6f3482de3b4e6459c70341e3aba3912a5f15eb0ea268b07c0ce4@ec2-52-44-55-63.compute-1.amazonaws.com:5432/deu74ncivoamea"
db = SQLAlchemy(app)


from bluethoughts import routes
