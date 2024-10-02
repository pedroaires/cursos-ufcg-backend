from sqlalchemy.orm import Session
from app.models.disciplina import Disciplina, prerequisitos

class DisciplinaRepository:

    @staticmethod
    def fetch_disciplinas_by_curriculo(db: Session, codigo_curso: str, codigo_curriculo: str):

        return db.query(Disciplina).filter(Disciplina.codigo_curso == codigo_curso).filter(Disciplina.codigo_curriculo == codigo_curriculo).all()
    
    @staticmethod
    def fetch_prerequisitos(db: Session, disciplinas_ids: list):
        return db.query(prerequisitos).filter(
            prerequisitos.c.disciplina_id.in_(disciplinas_ids)
        ).all()