from sqlalchemy import Column, Integer, String, ForeignKey
from app.utils.db import Base

curriculos_field_conversion = {
    'courseCode': 'codigo_curso',
    'curriculumCode': 'codigo_curriculo',
    'minNumberOfTerms': 'min_periodos',
    'maxNumberOfTerms': 'max_periodos',
    'minNumberOfEnrolledCredits': 'min_creditos_matriculados',
    'maxNumberOfEnrolledCredits': 'max_creditos_matriculados',
    'minMandatoryCreditsNeeded': 'min_creditos_obrigatorios',
    'minOptionalCreditsNeeded': 'min_creditos_optativos',
    'minComplementaryCreditsNeeded': 'min_creditos_complementares',
    'minAcademicsExtensionActivities': 'min_atividades_extensao'
}

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
