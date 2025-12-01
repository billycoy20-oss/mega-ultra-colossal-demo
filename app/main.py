from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .dashboard import render_dashboard
from .api import router as api_router

app = FastAPI()

# Rota API
app.include_router(api_router, prefix="/api")

# Arquivos estáticos (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home():
    return render_dashboard()
