import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from components import navbar
from pages import page1, page2

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True)

nav = navbar.Navbar()

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[
        html.H1('Home Page')
    ])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return html.Center(html.H1('Home Page'))
    elif pathname == '/page-1':
        return page1.layout
    elif pathname == '/page-2':
        return page2.layout
    else:
        return html.H1('404 No Page Found')


if __name__ == '__main__':
    app.run_server(debug=True)
