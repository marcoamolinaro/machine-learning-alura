from dash import Dash, dcc, html
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc
import joblib
import pandas as pd
import numpy as np

modelo = joblib.load('modelo_xgboost.pkl')
medianas = joblib.load('medianas.pkl')

app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP])

formulario = dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label("Idade"),
                    dbc.Input(id='idade', type='number',placeholder='Digite a idade'),
                ], className='mb-3'),
                dbc.CardGroup([
                dbc.Label("Sexo Biológico"),
                    dbc.Select(id='sexo', options=[
                        {'label': 'Masculino', 'value': '1'},
                        {'label': 'Feminino', 'value': '0'}
                    ]),
                ], className='mb-3'),
                # tipo de dor no peito
                dbc.CardGroup([
                    dbc.Label("Tipo de dor no peito"),
                    dbc.Select(id='cp', options=[
                        {'label': 'Angina típica', 'value': '1'},
                        {'label': 'Angina atípica', 'value': '2'},
                        {'label': 'Não angina', 'value': '3'},
                        {'label': 'Angina assintomático', 'value': '4'},
                    ], className='mb-3'),
                ]),
                # trestbps
                dbc.CardGroup([
                    dbc.Label('Pressão arterial em repouso'),
                    dbc.Input(id='trestbps', type='number', placeholder='Digite a pressão arterial')
                ], className='mb-3'),
                # chol
                dbc.CardGroup([
                    dbc.Label('Colesterol sério'),
                    dbc.Input(id='chol', type='number', placeholder='Digite a colesterol')
                ], className='mb-3'),
                # fbs
                dbc.CardGroup([
                    dbc.Label('Glicose em jejum'),
                    dbc.Select(id='fbs', options=[
                        {'label': 'Menor que 120 mg/dl', 'value': '0'},
                        {'label': 'Maior que 120 mg/dl', 'value': '1'},
                    ], className='mb-3'),
                ]),
                # restecg
                dbc.CardGroup([
                    dbc.Label("Eletrocardiografia em repouso"),
                    dbc.Select(id='restecg', options=[
                        {'label': 'Normal', 'value': '0'},
                        {'label': 'Anormalidades de ST-T', 'value': '1'},
                        {'label': 'Hipertrofia ventricular esquerda', 'value': '2'}
                    ]),
                ], className='mb-3'),
            ]),
            dbc.Col([
                # thalach
                dbc.CardGroup([
                    dbc.Label('Frequência cardíaca máxima'),
                    dbc.Input(id='thalach', type='number', placeholder='Digite a frequência cardíaca máxima')
                ], className='mb-3'),
                # exang
                dbc.CardGroup([
                    dbc.Label('Angina induzida por exercício'),
                    dbc.Select(id='exang', options=[
                        {'label': 'Sim', 'value': '1'},
                        {'label': 'Não', 'value': '0'},
                    ], className='mb-3'),
                ]), 
                # oldpeak
                dbc.CardGroup([
                    dbc.Label('Depressão do segmento ST induzida por exercício'),
                    dbc.Input(id='oldpeak', type='number', placeholder='Digite a depressão do segmento ST induzida por exercício')
                ], className='mb-3'),
                # slope
                dbc.CardGroup([
                    dbc.Label("Inclinação do segmento ST"),
                    dbc.Select(id='slope', options=[
                        {'label': 'Ascendente', 'value': '1'},
                        {'label': 'Plana', 'value': '2'},
                        {'label': 'Descendente', 'value': '3'},
                    ], className='mb-3'),
                ]),
                # ca
                dbc.CardGroup([
                    dbc.Label('Número de vasos principais coloridos por fluoroscopia'),
                    dbc.Select(id='ca', options=[
                        {'label': '0', 'value': '0'},
                        {'label': '1', 'value': '1'},
                        {'label': '2', 'value': '2'},
                        {'label': '3', 'value': '3'},
                    ], className='mb-3'),
                ], className='mb-3'),    
                # thal
                    dbc.CardGroup([
                    dbc.Label('Cintilografia do miocardio'),
                    dbc.Select(id='thal', options=[
                        {'label': 'Normal', 'value': '3'},
                        {'label': 'Defeito fixo', 'value': '6'},
                        {'label': 'Defeito reversível', 'value': '7'},
                    ], className='mb-3'),
                ], className='mb-3'),    
                # botão de submit para previsão
                dbc.CardGroup([
                    dbc.Button("Prever", id='botao-prever', color='primary', n_clicks=0)
                ], className='mb-3'),
            ]),
        ])
    ])

app.layout = html.Div([
    html.H1("Previsão de doença cardíaca"),
    formulario,
    html.Div(id='previsao')
])


@app.callback(
    Output('previsao', 'children'),
    [
        Input('botao-prever', 'n_clicks')
    ],
    [State('idade', 'value'),
    State('sexo', 'value'),
    State('cp', 'value'),
    State('trestbps', 'value'),
    State('chol', 'value'),
    State('fbs', 'value'),
    State('restecg', 'value'),
    State('thalach', 'value'),
    State('exang', 'value'),
    State('oldpeak', 'value'),
    State('slope', 'value'),
    State('ca', 'value'),
    State('thal', 'value')]
)
def prever_doenca(n_clicks, idade, sexo, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    if n_clicks == 0:
        return ''
    
    entradas_usuario = pd.DataFrame(
        data = [[idade, sexo, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
        columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    )

    # preencher os campos nulos ou em branco com as medianas
    entradas_usuario.fillna(medianas, inplace=True)
    
    # oldpeak é float
    entradas_usuario['oldpeak'] = entradas_usuario['oldpeak'].astype(np.float64)

    # os outros, converter números de string para int
    for col in entradas_usuario.columns:
        if col != 'oldpeadk':
            entradas_usuario[col] = entradas_usuario[col].astype(np.int64)

    previsao = modelo.predict(entradas_usuario)[0]

    if previsao == 1:
        return html.H2("Você tem doença cardíaca")
    
    return html.H2("Você não tem doença cardíaca")

# Run app
if __name__ == '__main__':
    app.run(debug=True)