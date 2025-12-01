from fastapi.responses import HTMLResponse
import plotly.graph_objects as go

def render_dashboard():
    fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[3, 1, 5], mode="lines+markers"))
    chart = fig.to_html(full_html=False)

    html = f"""
    <html>
        <head>
            <link rel="stylesheet" href="/static/style.css">
            <title>Painel — Élio</title>
        </head>

        <body>
            <div class="sidebar">
                <h2>🔥 Élio Painel 🔥</h2>
                <a href="/">Dashboard</a>
                <a href="/api/status">Status API</a>
            </div>

            <div class="content">
                <h1>Bem-vindo, Élio 😈🔥</h1>
                {chart}
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html)
