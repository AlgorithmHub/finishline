import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from blocks.block import Block

class OutputForm(Block):
    
#     base_id = 'output-form'
    
    def layout(self):
        return html.Div([
            html.Div(id=self.register('output-state'))
        ])
    
    @Block.require(['n_clicks'], state=['input1', 'input2'])
    def callback_outputState_children(self, n_clicks, input1, input2):
        return u'''
            The Button has been pressed {} times,
            Input 1 is "{}",
            and Input 2 is "{}"
        '''.format(n_clicks, input1, input2)  
    
    
class InputForm(Block):
    
#     base_id = 'input-form'
    
    def layout(self):
        return html.Div([
            dcc.Input(id=self.register('input-1-state'), type='text', value=self.data['state']),
            dcc.Input(id=self.register('input-2-state'), type='text', value=self.data['country']),
            html.Button(id=self.register('submit-button'), n_clicks=0, children='Submit')
        ])
    
    
class HelloWorld(Block):
    
#     base_id = 'hello-world'
    
    def layout(self):
        return html.Div([
            html.H1('FinishLine Proof of Concept')
        ])
    