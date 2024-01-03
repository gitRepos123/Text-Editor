from flask import Flask 
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
api = Api(app)




