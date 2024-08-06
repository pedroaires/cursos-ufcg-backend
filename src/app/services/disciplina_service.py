from sqlalchemy.orm import Session
from app.repositories.curso_repository import CursoRepository
from app.repositories.disciplina_repository import DisciplinaRepository
from app.models.pre_requisitos_model import PreRequisitos
class DisciplinaService:

    @staticmethod
    def get_mapa_pre_requisitos(disciplinas, pre_requisitos):
        mapa = {}
        for disciplina in disciplinas:
            disciplina_data = {
                'codigo_disciplina': disciplina.codigo_disciplina,
                'disciplina': disciplina.disciplina,
                'tipo': disciplina.tipo,
                'semestre': disciplina.semestre,
                'horas': disciplina.horas,
                'creditos': disciplina.creditos,
                'pre_requisitos': [],
                'pos_requisitos': []
            }
            mapa[disciplina.codigo_disciplina] = disciplina_data

        for prereq in pre_requisitos:
            cod_disc = prereq.codigo_disciplina
            cod_prereq = prereq.codigo_prerequisito

            if cod_disc in mapa:
                mapa[cod_disc]['pre_requisitos'].append(cod_prereq)
            if cod_prereq in mapa:
                mapa[cod_prereq]['pos_requisitos'].append(cod_disc)

        result = sorted(mapa.values(), key=lambda x: x['semestre'])
        return result

    @staticmethod
    def get_disciplina_from_course(db: Session, curso_schema: str):
        try:
            curso = CursoRepository.fetch_curso_by_schema(db, curso_schema)

            disciplinas = DisciplinaRepository.fetch_disciplinas_by_codigo_curso(db, curso.codigo_curso)
            curriculo = disciplinas[0].codigo_curriculo
            pre_requisitos = db.query(PreRequisitos).filter(PreRequisitos.codigo_curso == curso.codigo_curso).filter(PreRequisitos.codigo_curriculo == curriculo).all()

            return DisciplinaService.get_mapa_pre_requisitos(disciplinas, pre_requisitos)

        except:
            raise Exception("Curso não encontrado")
