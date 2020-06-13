from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = 'f8bcff1dc840085af10535ca4673c3a5'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://evznnauhsmzzgz:b41bc5a04b725c8bc57436cc50531b0c045bfc3682152a98a81108f9b8d78a29@ec2-34-194-198-176.compute-1.amazonaws.com:5432/dfmaaj5vr1v8it"
db = SQLAlchemy(app)


from bluethoughts import routes
