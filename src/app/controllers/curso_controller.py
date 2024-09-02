from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db
from pydantic import BaseModel
from app.services.curso_service import CursoService
from app.services.disciplina_service import DisciplinaService
from app.services.aluno_service import AlunoService
from app.services.historico_service import HistoricoService
from typing import List


router = APIRouter()

class CursoIndice(BaseModel):
    nome_comum: str
    schema: str
    campus: str

class InfoCursoResponse(BaseModel):
    codigo_curso: str
    nome_comum: str
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

class TaxaSucessoResponse(BaseModel):
    codigo_disciplina: str
    aprovados: int
    total: int
    periodo: float

class TaxaSucessoPeriodosResponse(BaseModel):
    min_periodo: float
    max_periodo: float

class FormandosResponse(BaseModel):
    periodo: float
    ingressos: int
    formandos: int

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

@router.get("/cursos/{curso}", response_model=InfoCursoResponse, summary="Informações de um curso")
def get_info_curso(curso: str, db: Session = Depends(get_db)) -> InfoCursoResponse:
    info_curso = CursoService.get_info_curso(db, curso)
    return InfoCursoResponse(
        codigo_curso=info_curso.codigo_curso,
        nome_comum=info_curso.nome_comum,
        campus=info_curso.campus
    )

@router.get("/cursos/{curso}/disciplinas", response_model=List[DisciplinaResponse], summary="Lista disciplinas de um curso")
def get_disciplinas_by_curso(curso: str, db: Session = Depends(get_db)) -> List[DisciplinaResponse]:
    disciplinas_data = DisciplinaService.get_disciplina_from_course(db, curso)
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

@router.get("/cursos/{curso}/taxa-sucesso", response_model=List[TaxaSucessoResponse], summary="Taxa de sucesso de um curso")
def get_taxa_sucesso(curso: str, db: Session = Depends(get_db)) -> List[TaxaSucessoResponse]:
    aprovacoes_data = HistoricoService.get_aprovacoes(db, curso)
    return [
        TaxaSucessoResponse(
            codigo_disciplina=aprovacao['codigo_disciplina'],
            aprovados=aprovacao['aprovados'],
            total=aprovacao['total'],
            periodo=aprovacao['periodo']
        ) for aprovacao in aprovacoes_data
    ]

@router.get("/cursos/{curso}/taxa-sucesso/periodos", response_model=TaxaSucessoPeriodosResponse, summary="Taxa de sucesso de um curso")
def get_taxa_sucesso_periodos(curso: str, db: Session = Depends(get_db)) -> TaxaSucessoPeriodosResponse:
    min, max = HistoricoService.get_min_max_periodos(db, curso)
    return TaxaSucessoPeriodosResponse(
        min_periodo=min,
        max_periodo=max
    )

@router.get("/cursos/{curso}/formandos", response_model=List[FormandosResponse] , summary="Formandos de um curso")
def get_ingressos_e_formandos(curso: str, db: Session = Depends(get_db)) -> List[FormandosResponse]:
    formandos_data = AlunoService.get_ingressos_e_formandos_por_periodo(db, curso)

    return [
        FormandosResponse(
            periodo=formando.periodo,
            ingressos=formando.ingressos,
            formandos=formando.formandos
        ) for formando in formandos_data
    ]