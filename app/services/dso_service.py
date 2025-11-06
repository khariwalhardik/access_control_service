from app.models import OfficeDSO, DSO
from app import db

def get_offices_by_dso(dso_id):
    """
    Return all office IDs that belong to a given DSO.
    """
    offices = OfficeDSO.query.filter_by(dso_id=dso_id).all()
    return [o.office_id for o in offices]


def get_dso_by_office(office_id):
    """
    Return the DSO that owns a given office.
    """
    office_dso = OfficeDSO.query.filter_by(office_id=office_id).first()
    if not office_dso:
        return None

    dso = DSO.query.get(office_dso.dso_id)
    return {"dso_id": dso.id, "dso_name": dso.name, "info": dso.info}
