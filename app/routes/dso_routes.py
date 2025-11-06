from flask import Blueprint, jsonify
from app.services.dso_service import get_offices_by_dso, get_dso_by_office

dso_bp = Blueprint("dso", __name__)

@dso_bp.route("/dso/<int:dso_id>/offices", methods=["GET"])
def get_offices_for_dso_route(dso_id):
    """List all office IDs under a given DSO."""
    offices = get_offices_by_dso(dso_id)
    if not offices:
        return jsonify({"message": "No offices found for this DSO"}), 404
    return jsonify({"dso_id": dso_id, "offices": offices})


@dso_bp.route("/offices/<int:office_id>/dso", methods=["GET"])
def get_dso_for_office_route(office_id):
    """Find which DSO a given office belongs to."""
    dso = get_dso_by_office(office_id)
    if not dso:
        return jsonify({"message": "Office not found or not mapped to any DSO"}), 404
    return jsonify(dso)
