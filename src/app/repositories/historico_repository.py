from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.historico import Historico

class HistoricoRepository:
    
    @staticmethod
    def fetch_historico_by_curso(db: Session, codigo_curso: str):
        return db.query(Historico).filter(Historico.codigo_curso == codigo_curso, Historico.codigo_curriculo).all()
    
    @staticmethod
    def fetch_min_max_periodos(db: Session, codigo_curso: str):
        return db.query(func.min(Historico.periodo), func.max(Historico.periodo)).filter(Historico.codigo_curso == codigo_curso).first()