from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Initialize extensions globally
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """Application factory function for Flask"""
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models AFTER db is initialized to register them
    from app import models  # This imports all models via app/models/__init__.py

    # Register all route blueprints
    from app.routes import all_blueprints
    for bp, prefix in all_blueprints:
        app.register_blueprint(bp, url_prefix=prefix)

    # Health check route for testing
    @app.route("/health", methods=["GET"])
    def health_check():
        return {"status": "ok", "message": "Access Control Service running"}

    return app
