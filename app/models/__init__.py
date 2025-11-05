from app import db

# Import all model classes
from .dso import DSO
from .office_dso import OfficeDSO
from .role import Role
from .permission import Permission
from .role_permission import RolePermission
from .user_office_role import UserOfficeRole
from .user_dso_role import UserDSORole

# Optional: list them for clarity
__all__ = [
    "DSO",
    "OfficeDSO",
    "Role",
    "Permission",
    "RolePermission",
    "UserOfficeRole",
    "UserDSORole"
]
