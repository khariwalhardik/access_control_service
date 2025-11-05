from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from .models import *

# Initialize DB globally
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models (so Flask knows about them before creating tables)
    from . import models

    # Example route to verify setup
    @app.route("/health")
    def health_check():
        return {"status": "ok", "message": "Access Control Service running"}

    return app
