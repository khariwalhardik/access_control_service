from src.models import UserOfficeRole, UserDSORole, Role

def get_user_roles(user_id):
    """
    Fetch all roles assigned to a user (DSO-level + Office-level).
    Returns a list of {role, office_id, dso_id}.
    """
    roles = []

    office_roles = (
        UserOfficeRole.query
        .filter_by(user_id=user_id)
        .join(Role, UserOfficeRole.role_id == Role.id)
        .add_columns(Role.title, UserOfficeRole.office_id,Role.id)
        .all()
    )

    dso_roles = (
        UserDSORole.query
        .filter_by(user_id=user_id)
        .join(Role, UserDSORole.role_id == Role.id)
        .add_columns(Role.title, UserDSORole.dso_id,Role.id)
        .all()
    )

    for role, title, office_id, role_id in office_roles:
        roles.append({
            "scope": "office",
            "role_id": role_id,
            "role": title,
            "office_id": office_id
        })

    for role, title, dso_id, role_id in dso_roles:
        roles.append({
            "scope": "dso",
            "role_id": role_id,
            "role": title,
            "dso_id": dso_id
        })

    return roles
