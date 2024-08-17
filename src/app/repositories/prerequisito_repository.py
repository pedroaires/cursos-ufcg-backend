from sqlalchemy.orm import Session
from app.models.prerequisito import Prerequisito

class PrerequisitoRepository:
    @staticmethod
    def fetch_prerequisitos_by_curriculo(db: Session, codigo_curso: str, codigo_curriculo: str):
        return db.query(Prerequisito).filter(Prerequisito.codigo_curso == codigo_curso, Prerequisito.codigo_curriculo == codigo_curriculo).all()
