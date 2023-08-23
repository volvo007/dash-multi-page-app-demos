import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
# import plotly.graph_objects as go
import plotly.express as px

import pandas as pd

import dash_bootstrap_components as dbc

from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__, server=server,
                url_base_pathname='/', external_stylesheets=[dbc.themes.BOOTSTRAP],)

options = {'foo': 'y1', 'bar': 'y2'}

df = pd.DataFrame({'y1': [1, 2, 3], 'y2': [4, 5, 6]})

app.layout = html.Div(
    [
        html.H1("Multi Page App Demo: Sharing data between pages",
                style={'textAlign': 'center'}),
        html.Hr(),
        dbc.Row(
            [dbc.Col(  # drop down menu based on options
                [dcc.Dropdown(
                    id='dropdown',
                    options=[{'label': k, 'value': v}
                             for k, v in options.items()],
                    value='y1', clearable=False,
                )], md=4,
                style={'display': 'inline-block',
                       'vertical-align': 'top'}),
             dbc.Col(
                [
                    dcc.Graph(id='graph'),
                ], md=8,
                style={'width': '60%', 'display': 'inline-block', 'padding': '0 10'}),
             ]),
    ], style={'width': '90%', 'margin': 'auto'})


@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')])
def update_graph(value):
    if value is None:
        raise PreventUpdate
    fig = px.line(df, y=value, markers=True, title='Test')
    fig.update_layout({'title': {'x': 0.5, 'font': {'size': 28}},
                       'margin': {'l': 0, 'b': 0, 'r': 0, 't': 50}})
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
