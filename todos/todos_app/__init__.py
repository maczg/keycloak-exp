from flask import Flask
from config import Config
from .database import redis, mongo
from .plugins import ma


def create_app(config=Config):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)

    # Init plugins
    mongo.init_app(app)
    redis.init_app(app)

    # # Marshmallow must be inited after SQLAlchemy
    ma.init_app(app)

    with app.app_context():
        # from . import routes
        return app
