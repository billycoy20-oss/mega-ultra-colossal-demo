from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status():
    return {
        "status": "online",
        "owner": "Élio",
        "message": "Painel está funcionando perfeitamente 😈🔥"
    }
