import os

from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)


app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

db = SQLAlchemy()


def create_app(script_info=None):

    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    from src.api.ping import ping_blueprint
    app.register_blueprint(ping_blueprint)

    from src.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # TODO: db doesn't work
    @app.shell_context_processor
    def ctx():
        return dict(app=app, db=db)

    return app
