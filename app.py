from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'hola mundo'
# holi

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration
app.config.from_object("config.DevelopmentConfig")


# ORM setup
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

# print(db)
ma = Marshmallow(app)


# Routes setup
import routes.riesgos_controller
import routes.auth

if __name__ == "__main__":
    app.run(debug=True)