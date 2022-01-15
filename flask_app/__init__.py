from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from flask_app.common_route import common_blueprint
from flask_app.user_route import user_blueprint

app.register_blueprint(common_blueprint)
app.register_blueprint(user_blueprint)
