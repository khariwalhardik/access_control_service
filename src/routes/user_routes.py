from flask import Blueprint, jsonify
from src.services.user_service import get_user_roles

user_bp = Blueprint("user", __name__)

@user_bp.route("/users/<int:user_id>/roles", methods=["GET"])
def get_user_roles_route(user_id):
    """Return all roles assigned to a specific user (DSO + Office)."""
    roles = get_user_roles(user_id)
    return jsonify({"user_id": user_id, "roles": roles})
