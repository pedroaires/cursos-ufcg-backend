from sqlalchemy import func, case
from sqlalchemy.orm import Session
from app.models.aluno import Aluno 

class AlunoRepository:
    
    @staticmethod
    def get_ingressos_e_formandos_por_periodo(db: Session, codigo_curso: str):
        query = (
            db.query(
                Aluno.periodo_ingressao.label('periodo'),
                func.count(Aluno.id_aluno).label('ingressos'),
                func.sum(
                    case(
                        (Aluno.codigo_evasao == 'GRADUADO', 1), 
                        else_=0
                        )
                ).label('formandos')
            )
            .filter(Aluno.codigo_curso == codigo_curso)
            .group_by(Aluno.periodo_ingressao)
        )
        
        return query.all()
        
