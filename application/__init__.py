from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['CAHCE-TYPE'] = 'Simple'
app.config['SQLALCHEMY_DATABASE_URI'] = ""
# cache = Cache(app)
db = SQLAlchemy(app)
myapi = Api(app)

from application import controllers, api
