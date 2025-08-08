from dash import Dash, dcc, html
from dash.dependencies import Output, Input, State

app = Dash(__name__)

app.layout = html.Div([
    # input de idade
    html.Label('Idade'),
    dcc.Input(id='idade', type='number', value=0),
    # botão de submit
    html.Button('Submeter', id='botao-submeter', n_clicks=0),
    # output de meses
    html.Div(id='output-meses')
])

@app.callback(
    output = Output('output-meses', 'children'),
    inputs=Input('botao-submeter', 'n_clicks'),
    state=State('idade', 'value'),
    prevent_initial_call=True
)
def calcula_meses(n_clicks, idade):
    if n_clicks == 0 or idade is None:
        return ''
    return idade * 12

# Run app
if __name__ == '__main__':
    app.run(debug=True)
