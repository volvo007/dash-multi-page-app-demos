# import dash
from dash import html
import dash_bootstrap_components as dbc

table_content = [
    ('Arthur', 'Dent'),
    ('Ford', 'Prefect'),
    ('Zaphod', 'Beeblebrox'),
    ('Tricia', 'McMillan')
]

table_header = [
    html.Thead(html.Tr([html.Th('First Name'), html.Th('Last Name')]))
]
table_body = [html.Tr([html.Td(a), html.Td(b)]) for a, b in table_content]

table = dbc.Table(table_header + table_body, bordered=True, color='primary',
                  dark=True, hover=True, responsive=True, striped=True)

layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1('Page 2')),
        html.Br(),
        html.Hr(),
        dbc.Col([
            html.H3('Column 1'),
            dbc.Button('Click Here', id='btn-2')
        ]),
        dbc.Col([
            html.H3('Column 2'),
            table
        ]),
    ]),
])
