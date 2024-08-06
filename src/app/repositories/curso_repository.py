from sqlalchemy.orm import Session
from app.models.curso_model import Curso

class CursoRepository:

    @staticmethod
    def fetch_cursos_ativos(db: Session):
        return db.query(Curso).filter(Curso.disponivel == True).all()
