from src import db

# Import all model classes
from .dso_model import DSO
from .office_dso_model import OfficeDSO
from .role_model import Role
from .permission_model import Permission
from .role_permission_model import RolePermission
from .user_office_role_model import UserOfficeRole
from .user_dso_role_model import UserDSORole

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
