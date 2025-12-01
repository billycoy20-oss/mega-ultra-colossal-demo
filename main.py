from fastapi import FastAPI
import numpy as np
import plotly.graph_objects as go

app = FastAPI()

@app.get("/")
def home():
    preco = np.linspace(10, 20, 50)
    sinal = np.where(preco > 15, "VENDA", "COMPRA")

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=preco, mode="lines", name="Preço"))
    html = fig.to_html(include_plotlyjs="cdn")

    return {"mensagem": "MEGA ULTRA COLOSSAL ONLINE",
            "sinais": sinal.tolist(),
            "grafico_html": html}
