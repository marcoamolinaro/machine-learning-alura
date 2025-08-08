from ucimlrepo import fetch_ucirepo
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Fetch dataset
heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features

# Create histogram figure (no .show() here!)
figura_histograma = px.histogram(dados, x='age', title='Histograma de idade')
div_do_histograma = html.Div([
        html.H2("Histograma de Idades"),
        dcc.Graph(figure=figura_histograma)
    ])

dados['doenca'] = (heart_disease.data.targets > 0) * 1
figura_boxplot = px.box(dados, x='doenca', y='age', title='Boxplot de Idades', color='doenca')
div_do_boxplot = html.Div([
        html.H2("Boxplot de Idades"),
        dcc.Graph(figure=figura_boxplot)
    ])

# Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Análise de dados do UCI Repository Heart Disease"),
    div_do_histograma,
    div_do_boxplot
])

# podemos adicionar de forma dinâmica mais elementos no gráfico
#app.layout.children.append(div_do_boxplot)

# Run app
if __name__ == '__main__':
    app.run(debug=True)
