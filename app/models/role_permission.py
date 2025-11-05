from app import db

class RolePermission(db.Model):
    __tablename__ = "role_permission"

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey("permission.id"), nullable=False)

    role = db.relationship("Role", back_populates="permissions")
    permission = db.relationship("Permission", back_populates="roles")
