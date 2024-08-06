from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db
from pydantic import BaseModel
from app.services.curso_service import CursoService
from typing import List


router = APIRouter()

class CursoIndice(BaseModel):
    nome_comum: str
    schema: str
    campus: str

@router.get("/", response_model=str, summary="Cursos UFCG HOME")
def home():
    return "HOME"

@router.get("/cursos", response_model=List[CursoIndice], summary="Lista cursos da UFCG")
def get_cursos(db: Session = Depends(get_db)) -> List[CursoIndice]:
    
    cursos = CursoService.get_cursos_ativos(db)
    return [
        CursoIndice(
            nome_comum=curso.nome_comum,
            schema=curso.schema,
            campus=curso.campus
        ) for curso in cursos
    ]