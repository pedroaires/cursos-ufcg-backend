from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.aprovacao import Aprovacao

class AprovacaoRepository:
    
    @staticmethod
    def fetch_aprovacoes_by_curso(db: Session, codigo_curso: str):
        return db.query(Aprovacao).filter(Aprovacao.codigo_curso == codigo_curso).all()
    
    @staticmethod
    def fetch_min_max_periodos(db: Session, codigo_curso: str):
        return db.query(func.min(Aprovacao.periodo), func.max(Aprovacao.periodo)).filter(Aprovacao.codigo_curso == codigo_curso).first()