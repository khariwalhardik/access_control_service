from flask import Blueprint, jsonify
# Assuming you have a service file to fetch data
from src.services.role_service import get_role_details, get_role_permissions 

role_bp = Blueprint("role", __name__)

@role_bp.route("/role/<int:role_id>", methods=["GET"])
def get_role_details_and_permissions_route(role_id):
    """List role details and all associated permissions for a given role ID."""
    
    # 1. Fetch Role Details (e.g., role name, description)
    # **NOTE**: You need to implement the get_role_details function in your service.
    role_details = get_role_details(role_id) 
    
    if not role_details:
        # Return a 404 Not Found if the role doesn't exist
        return jsonify({"message": f"Role with ID {role_id} not found"}), 404
        
    # 2. Fetch Permissions
    permissions = get_role_permissions(role_id)
    
    # 3. Combine and return the data
    response_data = {
        "role_id": role_id,
        "details": role_details, # This will be the role's name/description/etc.
        "permissions": permissions
    }
    
    return jsonify(response_data)