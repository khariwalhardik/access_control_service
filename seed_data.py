from app import create_app, db

# Import models *after* app context is ready
app = create_app()

with app.app_context():
    # Import models inside app context so db knows the app
    from app.models import (
        DSO, OfficeDSO,
        Role, Permission, RolePermission,
        UserOfficeRole, UserDSORole
    )

    print("🔹 Dropping and recreating tables...")
    db.drop_all()
    db.create_all()

    # ----- DSO -----
    dso1 = DSO(name="BrightSmiles Dental Group", info="Multi-office DSO in California")
    dso2 = DSO(name="HappyTeeth Network", info="DSO across Texas region")
    db.session.add_all([dso1, dso2])
    db.session.flush()  # get IDs

    # ----- Office Mapping -----
    o1 = OfficeDSO(office_id=101, dso_id=dso1.id)
    o2 = OfficeDSO(office_id=102, dso_id=dso1.id)
    o3 = OfficeDSO(office_id=201, dso_id=dso2.id)
    db.session.add_all([o1, o2, o3])

    # ----- Roles -----
    role_admin = Role(title="DSO Admin", description="Full access to all offices under DSO")
    role_manager = Role(title="Office Manager", description="Manages a single office")
    role_billing = Role(title="Billing Agent", description="Handles financial operations")
    role_readonly = Role(title="Read-only Staff", description="View-only access")
    db.session.add_all([role_admin, role_manager, role_billing, role_readonly])
    db.session.flush()

    # ----- Permissions -----
    p1 = Permission(name="view_patients", category="general")
    p2 = Permission(name="edit_records", category="clinical")
    p3 = Permission(name="view_billing", category="finance")
    p4 = Permission(name="edit_billing", category="finance")
    db.session.add_all([p1, p2, p3, p4])
    db.session.flush()

    # ----- Role–Permission mappings -----
    mappings = [
        RolePermission(role_id=role_admin.id, permission_id=p.id) for p in [p1, p2, p3, p4]
    ] + [
        RolePermission(role_id=role_manager.id, permission_id=p.id) for p in [p1, p2, p3]
    ] + [
        RolePermission(role_id=role_billing.id, permission_id=p.id) for p in [p3, p4]
    ] + [
        RolePermission(role_id=role_readonly.id, permission_id=p1.id)
    ]
    db.session.add_all(mappings)

    # ----- User Assignments -----
    u1 = UserDSORole(user_id=1, dso_id=dso1.id, role_id=role_admin.id)
    u2 = UserOfficeRole(user_id=2, office_id=101, role_id=role_manager.id)
    u3 = UserOfficeRole(user_id=3, office_id=102, role_id=role_billing.id)
    db.session.add_all([u1, u2, u3])

    db.session.commit()
    print("✅  Database seeded successfully!")
