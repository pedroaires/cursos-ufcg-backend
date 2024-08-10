from sqlalchemy.orm import Session
from app.models.disciplina import Disciplina

class DisciplinaRepository:

    @staticmethod
    def fetch_disciplinas_by_codigo_curso(db: Session, codigo_curso: str):
        # deve pegar apenas as disciplinas que tem o maior curriculo
        curriculo_atual = db.query(Disciplina).filter(Disciplina.codigo_curso == codigo_curso).order_by(Disciplina.codigo_curriculo.desc()).first().codigo_curriculo

        return db.query(Disciplina).filter(Disciplina.codigo_curso == codigo_curso).filter(Disciplina.codigo_curriculo == curriculo_atual).all()
