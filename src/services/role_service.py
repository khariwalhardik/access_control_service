from src.models import Role, Permission, RolePermission
from src import db
from sqlalchemy.orm.exc import NoResultFound

def get_role_details(role_id):
    """
    Return the name and description of the role by its ID.
    Returns None if the role is not found.
    """
    try:
        # Query the Role table for the specific role ID
        role = db.session.get(Role, role_id)
        # print('**********role service', role)
        
        if role:
            # Return a dictionary of key role attributes
            return {
                "name": role.title,
                "description": role.description,
            }
        return None
        
    except Exception as e:
        # In a real app, you might want more specific logging/error handling
        print(f"Error fetching role details for ID {role_id}: {e}")
        return None


def get_role_permissions(role_id):
    """
    Return a list of permission names associated with a given role.
    
    The original query is already functional but can be slightly simplified/clarified
    using SQLAlchemy relationships if defined, but sticking to explicit JOIN here.
    """
    # Check if the role actually exists before querying for permissions
    # (Optional, but good practice for efficiency)
    role_exists = db.session.get(Role, role_id)
    if not role_exists:
        return []

    # Use a subquery or the explicit join method
    role_perms = (
        db.session.query(Permission.name)
        .join(RolePermission, RolePermission.permission_id == Permission.id)
        .filter(RolePermission.role_id == role_id)
        .all()
    )
    
    # Extract the permission names from the list of tuples
    return [p[0] for p in role_perms]