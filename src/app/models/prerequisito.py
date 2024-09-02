from sqlalchemy import Column, String, ForeignKey
from app.utils.db import Base

class Prerequisito(Base):
    __tablename__ = "pre_requisitos"
    codigo_disciplina = Column(String, ForeignKey('disciplinas.codigo_disciplina'), primary_key=True)
    codigo_prerequisito = Column(String, ForeignKey('disciplinas.codigo_disciplina'), primary_key=True)
    codigo_curso = Column(String, ForeignKey('cursos.codigo_curso'), primary_key=True)
    codigo_curriculo = Column(String, index=True, primary_key=True)

    def __repr__(self):
        return f"Codigo_Disciplina: {self.codigo_disciplina}, Codigo_Prerequisito: {self.codigo_prerequisito}, Codigo_Curso: {self.codigo_curso}, Curriculo: {self.curriculo}"