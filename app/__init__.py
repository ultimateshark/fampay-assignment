
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

db = SQLAlchemy()


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "dev"])
    api = Api(app, title="My APP API", version="0.0.1")

    register_routes(api, app)
    db.init_app(app)
    return app