from sqlalchemy import Column, String, Boolean
from app.utils.db import Base

class Curso(Base):
    __tablename__ = "cursos"

    codigo_curso = Column(String, primary_key=True, index=True)
    nome_comum = Column(String, index=True)
    schema = Column(String, index=True)
    disponivel = Column(Boolean, default=True)
    campus = Column(String, index=True)

    def __repr__(self):
        return f"Curso: {self.nome_comum}, Codigo: {self.codigo_curso}, Campus: {self.campus}"