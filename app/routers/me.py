# Sessão sobre o desenvolvedor

from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
def me_session():
    return {"Desenvolvedor" : "Pedro Guilherme Pinheiro",
            "E-mail" : "guilhermepinheiro.work@gmail.com",
            "Curso" : "Sistemas da Informação",
            "Github" : "https://github.com/Gu1-all/",
            "Residência" : "Juazeiro do Norte - CE",
            "Interesses" : "Programação e Jogos"}