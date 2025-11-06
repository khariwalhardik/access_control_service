"""
app.services package

This package contains the core business logic for the Access Control Service.
Each file inside this folder represents a specific domain service such as:

- user_service.py       → user-role relationships, fetching user roles
- role_service.py       → role-permission mapping and definitions
- access_service.py     → ABAC + RBAC hybrid permission evaluation
- assign_role_service.py → role assignment and updates (future)
- dso_service.py        → DSO-level access and hierarchy (future)

Keeping each service isolated helps maintain a clean architecture and 
ensures the microservice can scale easily without tightly coupling logic.

Example usage:
    from app.services import check_permission
"""

# You can expose the most commonly used service functions here for convenience
from .access_service import check_permission
from .user_service import get_user_roles
from .role_service import get_role_permissions
from .dso_service import get_offices_by_dso, get_dso_by_office  # ✅ new service import

__all__ = [
    "check_permission",
    "get_user_roles",
    "get_role_permissions",
    "get_offices_by_dso",
    "get_dso_by_office"
]
