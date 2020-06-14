from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = 'f8bcff1dc840085af10535ca4673c3a5'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://jwosqyfhfemshm:ba16df90a62f15906e24efcd85eeb2998159a78820485d98482ec880eed2b135@ec2-18-213-176-229.compute-1.amazonaws.com:5432/d1uv744s883dai"
db = SQLAlchemy(app)


from bluethoughts import routes
