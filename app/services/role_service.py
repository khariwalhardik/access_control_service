from app.models import Role, Permission, RolePermission
from app import db

def get_role_permissions(role_id):
    """Return a list of permissions associated with a given role."""
    role_perms = (
        db.session.query(Permission.name)
        .join(RolePermission, RolePermission.permission_id == Permission.id)
        .filter(RolePermission.role_id == role_id)
        .all()
    )
    return [p[0] for p in role_perms]
