from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db
from pydantic import BaseModel
from app.services.curso_service import CursoService
from app.services.disciplina_service import DisciplinaService
from typing import List


router = APIRouter()

class CursoIndice(BaseModel):
    nome_comum: str
    schema: str
    campus: str

class DisciplinaResponse(BaseModel):
    codigo_disciplina: str
    disciplina: str
    tipo: str
    semestre: int
    horas: int
    creditos: int
    pre_requisitos: List[str]
    pos_requisitos: List[str]

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

@router.get("/{schema}/disciplinas", response_model=List[DisciplinaResponse], summary="Lista disciplinas de um curso")
def get_disciplinas_by_curso(schema: str, db: Session = Depends(get_db)) -> List[DisciplinaResponse]:
    print(f"aqui: {schema}")
    disciplinas_data = DisciplinaService.get_disciplina_from_course(db, schema)
    print(disciplinas_data)
    return [
        DisciplinaResponse(
            codigo_disciplina=disciplina['codigo_disciplina'],
            disciplina=disciplina['disciplina'],
            tipo=disciplina['tipo'],
            semestre=disciplina['semestre'],
            horas=disciplina['horas'],
            creditos=disciplina['creditos'],
            pre_requisitos=disciplina['pre_requisitos'],
            pos_requisitos=disciplina['pos_requisitos']
        ) for disciplina in disciplinas_data
    ]