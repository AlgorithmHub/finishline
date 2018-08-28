import dash_html_components as html
from dash.dependencies import Input, Output, State

def initialize(app, data, fl):
    
    fl.register_vis('OutputForm', html.Div(id='output-state'))

def finalize(app, data, fl):

    @app.callback(Output('output-state', 'children'),
                  [Input('submit-button', 'n_clicks')],
                  [State('input-1-state', 'value'),
                   State('input-2-state', 'value')])
    def update_output(n_clicks, input1, input2):
        return u'''
            The Button has been pressed {} times,
            Input 1 is "{}",
            and Input 2 is "{}"
        '''.format(n_clicks, input1, input2)
