"""
This is the starting file for the application.
"""

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from blog.models import db

migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevConfig")
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import auth
        from . import routes
        from .assets import compile_static_assets
        from blog.models.user import User

        # Register blueprints
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(routes.main_bp)

        # Compile static assets
        if app.config["FLASK_ENV"] == "development":
            compile_static_assets(app)

        return app
