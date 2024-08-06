from sqlalchemy.orm import Session
from app.repositories.curso_repository import CursoRepository

class CursoService:

    @staticmethod
    def get_cursos_ativos(db: Session):
        return CursoRepository.fetch_cursos_ativos(db)