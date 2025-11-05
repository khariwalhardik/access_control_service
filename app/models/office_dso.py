from app import db

class OfficeDSO(db.Model):
    __tablename__ = "office_dso"

    id = db.Column(db.Integer, primary_key=True)
    office_id = db.Column(db.Integer, nullable=False)  # from main app
    dso_id = db.Column(db.Integer, db.ForeignKey("dso.id"), nullable=False)

    dso = db.relationship("DSO", back_populates="offices")
