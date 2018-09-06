import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import random
import json
from dash.exceptions import PreventUpdate


def initialize(app, data, fl):
    @app.callback(
        Output('default-fl-page-layout', 'layouts'),
        [Input('fun-button', 'n_clicks')],
        [State('default-fl-page-layout', 'layouts'),
         State('default-fl-page-layout', 'breakpoint')])
    def fun_times(n_clicks, old_layout, breakpoint):

        if n_clicks is 0:
            raise PreventUpdate()

        new_layout = old_layout

        print('old_config', new_layout)
        print('breakpoint', breakpoint)

        order = [d['i'] for d in new_layout[breakpoint]]

        random.shuffle(order)

        print('order', order)

        for i,v in enumerate(order):
            new_layout[breakpoint][i]['i'] = str(v)

        print('new_layout', new_layout)

        return new_layout

    fl.register_vis(
        'Test Layout',
        html.Div([
            html.Button(id='fun-button', n_clicks=0, children='Randomize!')
        ])
    )
