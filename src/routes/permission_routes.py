from flask import Blueprint, jsonify
from src.models.permission_model import Permission  # import your model
from src import db

permission_bp = Blueprint("permission", __name__)

@permission_bp.route("/permissions", methods=["GET"])
def list_permissions():
    """List all permissions stored in the database."""
    permissions = Permission.query.all()

    # Convert SQLAlchemy objects → JSON-friendly dicts
    permission_list = [
        {
            "id": p.id,
            "name": p.name,
            "category": p.category
        }
        for p in permissions
    ]

    return jsonify({"count": len(permission_list), "permissions": permission_list}), 200
