from flask import Blueprint, jsonify

permission_bp = Blueprint("permission", __name__)

@permission_bp.route("/permissions", methods=["GET"])
def list_permissions():
    """(Optional) List all permissions in the system."""
    # Placeholder for later expansion
    permissions = [
        "view_patients",
        "edit_records",
        "view_billing",
        "edit_billing"
    ]
    return jsonify({"permissions": permissions})
