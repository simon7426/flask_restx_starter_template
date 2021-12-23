import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app_settings = os.environ.get("APP_SETTINGS", "project.config.DevelopmentConfig")
    app.config.from_object(app_settings)

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from project.api import api

    api.init_app(app)

    @app.shell_context_processor
    def ctx():  # pragma: no cover
        return {"app": app, "db": db}

    return app
