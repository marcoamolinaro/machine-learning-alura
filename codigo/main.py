from dash import Dash, dcc, html
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc
import pages
from app import app


navegacao = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Gráficos", href='/graficos')),
        dbc.NavItem(dbc.NavLink("Formulário", href='/formulario')),
    ],
    brand="SCM - CardioCare",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navegacao,
    html.Div(id='conteudo')
])

@app.callback(
    Output('conteudo', 'children'),
    [Input('url', 'pathname')]
)
def mostrar_pagina(pathname):
    if pathname == '/graficos':
        return pages.graficos.layout
    elif pathname == '/formulario': 
        return pages.formulario.layout
    else:
        return html.P('Página inicial')

# Run app
if __name__ == '__main__':
    app.run(debug=True)