from dash import html
import dash_bootstrap_components as dbc


layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1('Page 1')),
        html.Br(),
        html.Hr(),
        dbc.Col([
            html.H3('Column 1'),
            dbc.Button('Click Here', id='btn-1',
                       color='primary', className='mr-1'),
        ]),
        dbc.Col([
            html.H3('Column 2'),
            html.P('This is a paragraph'),
        ]),
    ]),
])
