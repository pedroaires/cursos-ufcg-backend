from sqlalchemy.orm import Session
from app.models.curriculo import Curriculo

class CurriculoRepository:

    @staticmethod
    def fetch_max_curriculo(db: Session, codigo_curso: str):
        return db.query(Curriculo).filter(Curriculo.codigo_curso == codigo_curso).order_by(Curriculo.codigo_curriculo.desc()).first()