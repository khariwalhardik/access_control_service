from datetime import datetime
from src import db

class UserDSORole(db.Model):
    __tablename__ = "user_dso_role"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    dso_id = db.Column(db.Integer, db.ForeignKey("dso.id"), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    dso = db.relationship("DSO", back_populates="user_roles")
    role = db.relationship("Role")
