from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db
from pydantic import BaseModel
from app.models.curso_model import Curso
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
    try:
        cursos = db.query(Curso).all()

        return [
            CursoIndice(
                nome_comum=curso.nome_comum,
                schema=curso.schema,
                campus=curso.campus
            ) for curso in cursos
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))