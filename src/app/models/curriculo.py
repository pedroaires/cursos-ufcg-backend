from sqlalchemy import Column, Integer, String, ForeignKey
from app.utils.db import Base

class Curriculo(Base):
    __tablename__ = "curriculos"
    codigo_curriculo = Column(String, primary_key=True, index=True)
    codigo_curso = Column(String, ForeignKey('cursos.codigo_curso'), primary_key=True, index=True)
    min_periodos = Column(Integer, index=True)
    max_periodos = Column(Integer, index=True)
    min_creditos_matriculados = Column(Integer, index=True)
    max_creditos_matriculados = Column(Integer, index=True)
    min_creditos_obrigatorios = Column(Integer, index=True)
    min_creditos_optativos = Column(Integer, index=True)
    min_creditos_complementares = Column(Integer, index=True)
    min_atividades_extensao = Column(Integer, index=True)
    
    def __repr__(self):
        return f"Curriculo: {self.codigo_curriculo}, Curso: {self.codigo_curso}"
