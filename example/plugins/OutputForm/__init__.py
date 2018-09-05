import dash_html_components as html
<<<<<<< HEAD
import dash_building_blocks as dbb
    

class OutputForm(dbb.Block):
    
    def layout(self):
        return html.Div([
            html.Div(id=self.register('output-state'))
        ])
    
    def callbacks(self, input_n_clicks, state_input1, state_input2):
        
        @self.app.callback(
            self.output('output-state', 'children'),
            [input_n_clicks],
            [state_input1, state_input2]
        )
        def update_output(n_clicks, input1, input2):
            return u'''
                The Button has been pressed {} times,
                Input 1 is "{}",
                and Input 2 is "{}"
            '''.format(n_clicks, input1, input2) 
            
            
def initialize(app, data, fl):
            
    output_form = OutputForm(app, data)
    
    fl.register_vis('OutputForm', output_form.layout)
    fl.blocks.register('output-form', output_form)
    
=======
from dash.dependencies import Input, Output, State

def initialize(app, data, fl):
>>>>>>> master
    
    fl.register_vis('OutputForm', html.Div(id='output-state'))

def finalize(app, data, fl):
<<<<<<< HEAD
            
    fl.blocks['output-form'].callbacks(
        fl.blocks['input-form'].input('submit-button', 'n_clicks'),
        fl.blocks['input-form'].state('input-1-state', 'value'),
        fl.blocks['input-form'].state('input-2-state', 'value'),
    )
=======

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
>>>>>>> master
