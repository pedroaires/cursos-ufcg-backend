from sqlalchemy.orm import Session
from sqlalchemy import func
from app.repositories.historico_repository import HistoricoRepository
from app.repositories.curso_repository import CursoRepository

class HistoricoService:
    
    @staticmethod
    def get_aprovacoes(db: Session, curso_schema: str):
        curso = CursoRepository.fetch_curso_by_schema(db, curso_schema)
        historico = HistoricoRepository.fetch_historico_by_curso(db, curso.codigo_curso)
        aprovacoes = HistoricoService.__compute_aprovacoes(historico)
        return aprovacoes.values()
    
    @staticmethod
    def get_min_max_periodos(db: Session, curso_schema: str):
        curso = CursoRepository.fetch_curso_by_schema(db, curso_schema)
        min_periodo, max_periodo = HistoricoRepository.fetch_min_max_periodos(db, curso.codigo_curso)
        return min_periodo, max_periodo
    

    def __compute_aprovacoes(historico):
        aprovacoes_dict = {}
        for h in historico:
            key = (h.periodo, h.codigo_disciplina)
            if key not in aprovacoes_dict:
                aprovacoes_dict[key] = {'codigo_disciplina': h.codigo_disciplina, 'periodo': h.periodo, 'aprovados': 0, 'total': 0}
            
            aprovacoes_dict[key]['total'] += 1
            if h.situacao == 'APROVADO':
                aprovacoes_dict[key]['aprovados'] += 1
        return aprovacoes_dict