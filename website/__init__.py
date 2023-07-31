from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sihfshiajdoshioac'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:193720@localhost:5432/zahara'
    db.init_app(app)

    from website.views import views
    app.register_blueprint(views, url_prefix='/')
   

    return app

  