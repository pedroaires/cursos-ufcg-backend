from sqlalchemy.orm import Session
from app.repositories.curso_repository import CursoRepository
from app.repositories.disciplina_repository import DisciplinaRepository
from app.repositories.curriculo_repository import CurriculoRepository
import heapq

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
            mapa[disciplina.id] = disciplina_data
        id_to_codigo = {disciplina.id: disciplina.codigo_disciplina for disciplina in disciplinas}
        for prereq in pre_requisitos:
            disc_id = prereq.disciplina_id
            prereq_id = prereq.prerequisito_id

            if disc_id in mapa:
                mapa[disc_id]['pre_requisitos'].append(id_to_codigo[prereq_id])
            if prereq_id in mapa:
                if disc_id in id_to_codigo:
                    # significa que o prereq nao é uma disciplina optativa
                    # entao mapeamos os seus posrequisitos
                    mapa[prereq_id]['pos_requisitos'].append(id_to_codigo[disc_id])
        result = sorted(mapa.values(), key=lambda x: x['semestre'])
        return result

    @staticmethod
    def get_disciplina_from_course(db: Session, curso_schema: str):
        try:
            curso = CursoRepository.fetch_curso_by_schema(db, curso_schema)
            curriculo_atual = CurriculoRepository.fetch_max_curriculo(db, curso.codigo_curso)

            disciplinas = DisciplinaRepository.fetch_disciplinas_by_curriculo(db, curso.codigo_curso, curriculo_atual.codigo_curriculo)

            pre_requisitos = DisciplinaRepository.fetch_prerequisitos(db, [disc.id for disc in disciplinas])

            discs_s_optativas = [disc for disc in disciplinas if disc.tipo != 'OPCIONAL']

            discs_and_prereqs = DisciplinaService.get_mapa_pre_requisitos(discs_s_optativas, pre_requisitos)

            disciplinas_optativas = DisciplinaService.__add_optativas(discs_and_prereqs, curriculo_atual.min_creditos_optativos, semestre_field='semestre', creditos_field='creditos')
            
            disciplinas_data = discs_and_prereqs + disciplinas_optativas
            
            return sorted(disciplinas_data, key=lambda x: x['semestre'])

        except Exception as e:
            raise Exception(f"Algo deu errado ao buscar as disciplinas: {str(e)}")

    def __add_optativas(disciplinas_data, min_creditos_optativas, semestre_field='semestre', creditos_field='creditos'):
        """
        Método para definir um período ideal para as disciplinas optativas.
        Aloca as disciplinas nos períodos que possuem menos créditos.
        """
        creditos_por_semestre = DisciplinaService.__get_creditos_por_semestre(disciplinas_data, semestre_field, creditos_field)
        creditos_semestre_heap = [(creditos, semestre) for semestre, creditos in creditos_por_semestre.items()]
        heapq.heapify(creditos_semestre_heap)
        
        num_optativas, creditos_optativa, creditos_faltando = DisciplinaService.__calcular_numero_optativas(min_creditos_optativas)
        
        disciplinas_optativas = DisciplinaService.__distribuir_optativas(
            num_optativas, creditos_faltando, creditos_optativa, creditos_semestre_heap
        )

        return disciplinas_optativas


    def __get_creditos_por_semestre(disciplinas_data, semestre_field, creditos_field):
        """
        Função que retorna o total de créditos por semestre, dado o conjunto de disciplinas.
        """
        creditos_por_semestre = {}
        for disc in disciplinas_data:
            semestre = disc[semestre_field]
            creditos = disc[creditos_field]
            if semestre == -1:
                continue
            if semestre not in creditos_por_semestre:
                creditos_por_semestre[semestre] = 0
            creditos_por_semestre[semestre] += creditos
        return creditos_por_semestre


    def __calcular_numero_optativas(min_creditos_optativas):
        """
        Função que calcula o número de disciplinas optativas necessárias e créditos faltando.
        """
        creditos_optativa = 4
        num_optativas = min_creditos_optativas // creditos_optativa
        creditos_faltando = min_creditos_optativas % creditos_optativa

        if creditos_faltando > 0:
            num_optativas += 1
        
        return num_optativas, creditos_optativa, creditos_faltando


    def __distribuir_optativas(num_optativas, creditos_faltando, creditos_optativa, creditos_semestre_heap):
        """
        Função que distribui disciplinas optativas nos semestres com menos créditos.
        """
        disciplinas_optativas = []
        COD_FAKE = 9999999

        for i in range(num_optativas):
            valor_credito = creditos_faltando if i == num_optativas - 1 and creditos_faltando > 0 else creditos_optativa
            min_semestre = heapq.heappop(creditos_semestre_heap)
            creditos = min_semestre[0]
            semestre = min_semestre[1]

            optativa = {
                'codigo_disciplina': str(COD_FAKE - i),
                'disciplina': 'OPCIONAL',
                'tipo': 'OPCIONAL',
                'semestre': semestre,
                'horas': valor_credito * 15,
                'creditos': valor_credito,
                'pre_requisitos': [],
                'pos_requisitos': []
            }

            disciplinas_optativas.append(optativa)
            updated_semestre = (creditos + valor_credito, semestre)
            heapq.heappush(creditos_semestre_heap, updated_semestre)

        return disciplinas_optativas