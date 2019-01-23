import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
   html.H2('graph-2'),
    dcc.Dropdown(
        id='graph-2-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='graph-2-display-value'),
    html.Br(),
    dcc.Link('Navigate to the index', href='/'),
    html.Br(),
    dcc.Link('Navigate to graph-1', href='/apps/app1'),

])

@app.callback(Output('graph-2-display-value', 'children'),
              [Input('graph-2-dropdown', 'value')])
def display_value(value):
    print('display_value')
    return 'You have selected "{}"'.format(value)
