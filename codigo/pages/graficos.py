from ucimlrepo import fetch_ucirepo
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# Fetch dataset
heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features

# Create histogram figure (no .show() here!)
figura_histograma = px.histogram(dados, x='age', title='Histograma de idade')
div_do_histograma = html.Div([
        dcc.Graph(figure=figura_histograma)
    ])


dados['doenca'] = (heart_disease.data.targets > 0) * 1
figura_boxplot = px.box(dados, x='doenca', y='age', title='Boxplot de Idades', color='doenca')
div_do_boxplot = html.Div([
        dcc.Graph(figure=figura_boxplot)
    ])

# adicionando novos gráficos
figura_boxplot_chol = px.box(dados, x='doenca', y='chol', color='doenca', title='Boxplot de Colesterol Sérico')
div_do_boxplot_chol = html.Div([
    dcc.Graph(figure=figura_boxplot_chol)
])

figura_boxplot_trestbps = px.box(dados, x='doenca', y='trestbps', color='doenca', title='Pressão sanguínea em repouso')
div_do_boxplot_trestbps = html.Div([
    dcc.Graph(figure=figura_boxplot_trestbps)
])

layout = html.Div([
    html.H1("Análise de dados do UCI Repository Heart Disease", className='text-center mb=5'),
    dbc.Container([
        dbc.Row([
            dbc.Col([div_do_histograma, div_do_boxplot_chol], md=6),
            dbc.Col([div_do_boxplot, div_do_boxplot_trestbps], md=6)
        ])
    ])
])
