from dash import Dash, dcc, html
from dash.dependencies import Output, Input, State


app = Dash(__name__, external_stylesheets=['assets/main.css'])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Nav([
        dcc.Link('Gráficos', href='/graficos'),
        dcc.Link('Formulário', href='/formulário'),
    ]),
    html.Div(id='conteudo')
])

@app.callback(
    Output('conteudo', 'children'),
    [Input('url', 'pathname')]
)
def mostrar_pagina(pathname):
    if pathname == '/formulario':
        return html.P('formulario')
    elif pathname == '/graficos':
        return html.P('graficos')
    else:
        return html.P('Página inicial')

# Run app
if __name__ == '__main__':
    app.run(debug=True)