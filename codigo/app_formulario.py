from dash import Dash, dcc, html
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc

app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1("Previsão de doença cardíaca"),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label("Idade"),
                    dbc.Input(id='idade', type='number',placeholder='Digite a idade'),
                ], className='mb-3'),
                dbc.CardGroup([
                dbc.Label("Sexo Biológico"),
                    dbc.Select(id='sexo', options=[
                        {'label': 'Masculino', 'value': 'M'},
                        {'label': 'Feminino', 'value': 'F'}
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
                # restceg
                dbc.CardGroup([
                    dbc.Label('Eletrocardiografia em repouso'),
                    dbc.Select(id='restceg', options=[
                        {'label': 'Sim', 'value': '1'},
                        {'label': 'Não', 'value': '0'},
                    ], className='mb-3'),
                ]), 
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
                    dbc.Input(id='exang', type='number', placeholder='Digite a angina induzida por exercício')
                ], className='mb-3'),
                # oldpeak
                dbc.CardGroup([
                    dbc.Label('Depressão do segmento ST induzida por exercício'),
                    dbc.Input(id='oldpeak', type='number', placeholder='Digite a depressão do segmento ST induzida por exercício')
                ], className='mb-3'),
                # slope
                dbc.CardGroup([
                    dbc.Label("Inclinação do segmento sT"),
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
                    dbc.Button("Prever", id='botao-prever', color='primary')
                ], className='mb-3'),

            ]),
        ])
    ])

])




# Run app
if __name__ == '__main__':
    app.run(debug=True)