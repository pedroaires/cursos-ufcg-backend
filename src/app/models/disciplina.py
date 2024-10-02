from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.utils.db import Base

prerequisitos = Table(
    'prerequisitos', Base.metadata,
    Column('disciplina_id', String, ForeignKey('disciplinas.id', ondelete="CASCADE")),
    Column('prerequisito_id', String, ForeignKey('disciplinas.id', ondelete="CASCADE")),
    Column('condicao', String, index=True),
    Column('ordem_prioridade', Integer, index=True),
    Column('tipo', String, index=True),
    Column('operador', String, index=True)
)

class Disciplina(Base):
    __tablename__ = "disciplinas"
    id = Column(String, primary_key=True, index=True)
    codigo_disciplina = Column(String, index=True)
    disciplina = Column(String, index=True)
    creditos = Column(Integer, index=True)
    horas = Column(Integer, index=True)
    tipo = Column(String, index=True)
    semestre = Column(Integer, index=True)
    codigo_curriculo = Column(String, index=True)
    codigo_curso = Column(String, index=True)

    prerequisitos = relationship(
        "Disciplina",
        secondary=prerequisitos,
        primaryjoin=id==prerequisitos.c.disciplina_id,
        secondaryjoin=id==prerequisitos.c.prerequisito_id,
        backref="dependentes"
    )