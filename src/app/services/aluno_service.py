from sqlalchemy.orm import Session
from app.repositories.aluno_repository import AlunoRepository
from app.repositories.curso_repository import CursoRepository

class AlunoService:
    
    @staticmethod
    def get_ingressos_e_formandos_por_periodo(db: Session, curso: str):
        codigo_curso = CursoRepository.fetch_curso_by_schema(db, curso).codigo_curso
        return AlunoRepository.get_ingressos_e_formandos_por_periodo(db, codigo_curso)