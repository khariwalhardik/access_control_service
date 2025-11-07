from src.services.user_service import get_user_roles
from src.services.role_service import get_role_permissions
from src.models import OfficeDSO

def check_permission(user_id, office_id, action):
    """
    ABAC + RBAC hybrid permission evaluator.
    Handles:
      - office-level roles
      - DSO-level roles that cover multiple offices
    """
    user_roles = get_user_roles(user_id)
    reason = "Insufficient permissions"
    for role in user_roles:
        scope = role.get("scope")
        role_id = role.get("role_id")
        permissions = get_role_permissions(role_id)

        # Case 1️ — Office-level role
        if scope == "office" and role.get("office_id") == office_id:
            if action in permissions:
                return {"allowed": True, "granted_by_role": role.get("role")}
        
        # Case 2 — DSO-level role (covers multiple offices)
        elif scope == "dso":
            dso_id = role.get("dso_id")
            # Check if the office belongs to this DSO
            office_dso = OfficeDSO.query.filter_by(office_id=office_id, dso_id=dso_id).first()
            if office_dso:
                if action in permissions:
                    return {"allowed": True, "granted_by_role": f"{role.get('role')} (DSO Level)"}
    # If no rule matched
    return {"allowed": False, "reason": reason}
