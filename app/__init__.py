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

    # Import models inside the app context to register them
    with app.app_context():
        from .models import (
            DSO,
            OfficeDSO,
            Role,
            Permission,
            RolePermission,
            UserOfficeRole,
            UserDSORole
        )
        # Note: No need to 'pass' here — just importing is enough to register models

    # Health check route for testing
    @app.route("/health")
    def health_check():
        return {"status": "ok", "message": "Access Control Service running"}

    return app
