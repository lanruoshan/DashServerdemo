import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import flask
from app import app
from apps import app1, app2






url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([
    html.H2('Index'),
    dcc.Link('Navigate to graph-1', href='/apps/app1'),
    html.Br(),
    dcc.Link('Navigate to graph-2', href='/apps/app2'),
],style={'position':'absolute','left': '50%','top': '20%','-webkit-transform': 'translateX(-50%)',
         'transform': 'translateX(-50%)','height':'100%'})


def serve_layout():
    if flask.has_request_context():
        return url_bar_and_content_div
    return html.Div([
        url_bar_and_content_div,
        layout_index,
        app1.layout,
        app2.layout,

    ])
app.layout = serve_layout
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/apps/app1':
         return app1.layout
    elif pathname == '/apps/app2':
         return app2.layout
    else:
        return layout_index

if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix

    server.wsgi_app = ProxyFix(server.wsgi_app)

    app.run_server(debug=True,host='0.0.0.0')
