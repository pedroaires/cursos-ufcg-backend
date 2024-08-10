from sqlalchemy.orm import Session
from app.models.curso import Curso

class CursoRepository:

    @staticmethod
    def fetch_cursos_ativos(db: Session):
        return db.query(Curso).filter(Curso.disponivel == True).all()
    
    @staticmethod
    def fetch_curso_by_schema(db: Session, schema: str):
        return db.query(Curso).filter(Curso.schema == schema).first()
