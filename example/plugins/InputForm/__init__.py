from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import json

def initialize(app, data, fl):

    # finish line client side data api
    fl.register_data('output-form-n-clicks', { 'n_clicks': 0 })

    # plugin api to register visualization
    fl.register_vis(
        'InputForm',
        html.Div([
            dcc.Input(id='input-1-state', type='text', value=data['state']),
            dcc.Input(id='input-2-state', type='text', value=data['country']),
            html.Button(id='submit-button', n_clicks=0, children='Submit')
        ])
    )

def finalize(app, data, fl):

    # example callback that updates client side data
    @app.callback(Output('output-form-n-clicks', 'children'),
                  [Input('submit-button', 'n_clicks')])
    def callback(n_clicks):
        return json.dumps({ 'n_clicks': n_clicks })

