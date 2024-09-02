from sqlalchemy import Column, String, Float, ForeignKey
from app.utils.db import Base

class Historico(Base):
    __tablename__ = "historicos"
    # Como estamos usando dados anominizados, a matricula é fake
    matricula_fake = Column(String, primary_key=True, index=True)
    codigo_curso = Column(String, ForeignKey('cursos.codigo_curso'), primary_key=True)
    codigo_disciplina = Column(String, ForeignKey('disciplinas.codigo_disciplina'), primary_key=True)
    periodo = Column(Float, primary_key=True)
    media = Column(Float, index=True)
    situacao = Column(String, index=True)

    def __repr__(self):
        return f"Matricula: {self.matricula_fake}, Disciplina: {self.codigo_disciplina}, Periodo: {self.periodo}, Media: {self.media}, Situacao: {self.situacao}"