from datetime import datetime
from src import db

class DSO(db.Model):
    __tablename__ = "dso"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    info = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    offices = db.relationship("OfficeDSO", back_populates="dso")
    user_roles = db.relationship("UserDSORole", back_populates="dso")
