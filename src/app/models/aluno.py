from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.utils.db import Base

class Aluno(Base):
    __tablename__ = "alunos"
    id_aluno = Column(Integer, primary_key=True, index=True)
    periodo_ingressao = Column(Float, index=True)
    motivo_inatividade = Column(String, index=True)
    codigo_curso = Column(String, ForeignKey('cursos.codigo_curso'), index=True)
    situacao = Column(String, index=True)

    def __repr__(self):
        return f"Aluno: {self.id_aluno}, Periodo de Ingressao: {self.periodo_ingressao}, Curso: {self.codigo_curso}, Evasao: {self.codigo_evasao}"