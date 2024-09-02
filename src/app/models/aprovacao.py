from sqlalchemy import Column, String, Integer, Float, ForeignKey
from app.utils.db import Base

class Aprovacao(Base):
    __tablename__ = "aprovacoes"
    codigo_curso = Column(String, ForeignKey('cursos.codigo_curso'), primary_key=True)
    codigo_disciplina = Column(String, ForeignKey('disciplinas.codigo_disciplina'), primary_key=True)
    periodo = Column(Float, primary_key=True)
    aprovados = Column(Integer)
    total = Column(Integer)

    def __repr__(self):
        return f"Disciplina: {self.codigo_disciplina}, Periodo: {self.periodo}, Aprovados: {self.aprovados}, Total: {self.total}"