from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.utils.db import Base

class Disciplina(Base):
    __tablename__ = "disciplinas"
    codigo_disciplina = Column(String, primary_key=True, index=True)
    disciplina = Column(String, index=True)
    creditos = Column(Integer, index=True)
    horas = Column(Integer, index=True)
    tipo = Column(String, index=True)
    semestre = Column(Integer, index=True)
    codigo_curriculo = Column(String, index=True)
    codigo_curso = Column(String, ForeignKey('cursos.codigo_curso'))

    def __repr__(self):
        return f"Disciplina: {self.disciplina}, Codigo: {self.codigo_disciplina}"