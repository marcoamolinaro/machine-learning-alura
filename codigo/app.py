from ucimlrepo import fetch_ucirepo
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Fetch dataset
heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features

# Create histogram figure (no .show() here!)
figura_histograma = px.histogram(dados, x='age', title='Histograma de idade')

# Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Análise de dados do UCI Repository Heart Disease"),
    dcc.Graph(figure=figura_histograma)
])

# Run app
if __name__ == '__main__':
    app.run(debug=True)
    