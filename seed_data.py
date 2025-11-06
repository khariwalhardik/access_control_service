from app import create_app, db

app = create_app()

with app.app_context():
    from app.models import (
        DSO, OfficeDSO,
        Role, Permission, RolePermission,
        UserOfficeRole, UserDSORole
    )

    print("🔹 Dropping and recreating tables...")
    db.drop_all()
    db.create_all()

    # -----------------------------
    # 1️⃣ DSO (Dental Service Organizations)
    # -----------------------------
    dso1 = DSO(name="BrightSmiles Dental Group", info="Multi-office DSO in California")
    dso2 = DSO(name="HappyTeeth Network", info="DSO across Texas region")
    db.session.add_all([dso1, dso2])
    db.session.flush()  # So IDs are available

    # -----------------------------
    # 2️⃣ Offices under each DSO
    # -----------------------------
    offices = [
        OfficeDSO(office_id=101, dso_id=dso1.id),
        OfficeDSO(office_id=102, dso_id=dso1.id),
        OfficeDSO(office_id=103, dso_id=dso1.id),
        OfficeDSO(office_id=201, dso_id=dso2.id),
        OfficeDSO(office_id=202, dso_id=dso2.id)
    ]
    db.session.add_all(offices)

    # -----------------------------
    # 3️⃣ Roles
    # -----------------------------
    role_admin = Role(title="DSO Admin", description="Full access to all offices under DSO")
    role_manager = Role(title="Office Manager", description="Manages a single office")
    role_billing = Role(title="Billing Agent", description="Handles financial operations")
    role_readonly = Role(title="Read-only Staff", description="View-only access")
    db.session.add_all([role_admin, role_manager, role_billing, role_readonly])
    db.session.flush()

    # -----------------------------
    # 4️⃣ Permissions
    # -----------------------------
    p1 = Permission(name="view_patients", category="general")
    p2 = Permission(name="edit_records", category="clinical")
    p3 = Permission(name="view_billing", category="finance")
    p4 = Permission(name="edit_billing", category="finance")
    p5 = Permission(name="manage_staff", category="admin")
    db.session.add_all([p1, p2, p3, p4, p5])
    db.session.flush()

    # -----------------------------
    # 5️⃣ Role–Permission mappings
    # -----------------------------
    mappings = [
        # Admin → all permissions
        *[RolePermission(role_id=role_admin.id, permission_id=p.id) for p in [p1, p2, p3, p4, p5]],
        # Manager → operational + patient permissions
        *[RolePermission(role_id=role_manager.id, permission_id=p.id) for p in [p1, p2, p3]],
        # Billing → finance only
        *[RolePermission(role_id=role_billing.id, permission_id=p.id) for p in [p3, p4]],
        # Read-only → basic view
        RolePermission(role_id=role_readonly.id, permission_id=p1.id)
    ]
    db.session.add_all(mappings)

    # -----------------------------
    # 6️⃣ User Assignments
    # -----------------------------
    # DSO-level users
    u1 = UserDSORole(user_id=1, dso_id=dso1.id, role_id=role_admin.id)  # Full admin for BrightSmiles
    u2 = UserDSORole(user_id=2, dso_id=dso2.id, role_id=role_billing.id)  # Full admin for HappyTeeth

    # Office-level users
    u3 = UserOfficeRole(user_id=3, office_id=1, role_id=role_manager.id)
    u4 = UserOfficeRole(user_id=4, office_id=2, role_id=role_billing.id)
    u5 = UserOfficeRole(user_id=5, office_id=3, role_id=role_readonly.id)

    # Mixed access (one user in multiple offices)
    u6 = UserOfficeRole(user_id=6, office_id=4, role_id=role_manager.id)
    u7 = UserOfficeRole(user_id=6, office_id=5, role_id=role_billing.id)  # same user, multiple offices

    # Mulit-dso admin
    u8 = UserDSORole(user_id=7, dso_id=dso1.id, role_id=role_admin.id)
    u9 = UserDSORole(user_id=7, dso_id=dso2.id, role_id=role_admin.id)

    db.session.add_all([u1, u2, u3, u4, u5, u6, u7,u8,u9])

    db.session.commit()
    print("✅ Database seeded successfully with enhanced data!")
