from flask import Blueprint, jsonify, request
from src.services.access_service import check_permission

access_bp = Blueprint("access", __name__)

@access_bp.route("/check-permission", methods=["POST"])
def check_permission_route():
    """Check if a user is allowed to perform an action."""
    data = request.get_json()

    user_id = data.get("userId")
    office_id = data.get("officeId")
    action = data.get("action")

    if not all([user_id, office_id, action]):
        return jsonify({"error": "Missing required fields"}), 400

    result = check_permission(user_id, office_id, action)
    return jsonify(result)
