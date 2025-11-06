from flask import Blueprint, jsonify
from app.services.role_service import get_role_permissions

role_bp = Blueprint("role", __name__)

@role_bp.route("/roles/<int:role_id>/permissions", methods=["GET"])
def get_role_permissions_route(role_id):
    """List all permissions associated with a given role."""
    permissions = get_role_permissions(role_id)
    return jsonify({"role_id": role_id, "permissions": permissions})
