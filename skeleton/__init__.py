from flask import Flask, render_template
from flask_compress import Compress
from flask_sqlalchemy import SQLAlchemy
from os import path
from .config import config

db = SQLAlchemy()
compress = Compress()
g_app = None


def create_app():
    global g_app

    app = Flask(__name__)
    app.config.from_object(config["development"])

    db.init_app(app)

    g_app = app

    from .frontend.views import views
    from .frontend.js.routing import js_views

    from .models import User

    def page_not_found(e):
        return render_template("errors/404.html"), 404

    def method_not_allowed(e):
        return render_template("errors/405.html"), 405

    def too_many_requests(e):
        return render_template("errors/429.html"), 429

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(429, too_many_requests)

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(js_views, url_prefix="/js/")

    app.app_context().push()
    db.create_all()

    compress.init_app(app)

    return app


def indent_app(app):
    return app
