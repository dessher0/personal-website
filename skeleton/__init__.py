from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from .config import config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    db.init_app(app)

    from .views import views

    def page_not_found(e):
        return render_template('parts/error_404.html'), 404

    app.register_error_handler(404, page_not_found)
    app.register_blueprint(views, url_prefix='/')
    create_database(app)

    return app


def create_database(app):
    if not path.exists('skeleton/databases/database.db'):
        db.create_all(app=app)
    else:
        pass
