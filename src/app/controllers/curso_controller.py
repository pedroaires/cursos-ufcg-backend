from fastapi import APIRouter


router = APIRouter()

@router.get("/", response_model=str, summary="Cursos UFCG HOME")
def home():
    return "HOME"