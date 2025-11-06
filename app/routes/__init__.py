from .user_routes import user_bp
from .role_routes import role_bp
from .permission_routes import permission_bp
from .access_routes import access_bp
from .dso_routes import dso_bp  # ✅ new

all_blueprints = [
    (user_bp, "/api"),
    (role_bp, "/api"),
    (permission_bp, "/api"),
    (access_bp, "/api"),
    (dso_bp, "/api")  # ✅ add new route
]
