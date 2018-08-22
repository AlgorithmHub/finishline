# from dash.dependencies import Input, Output
# import json

# def layout(app, data, fl):

#     # finish line client side data api
#     fl.register_data('output-form-n-clicks', { 'n_clicks': 0 })

#     # plugin api to register visualization
#     fl.register_vis(
#         'InputForm',
#         html.Div([
#             dcc.Input(id='input-1-state', type='text', value=data['state']),
#             dcc.Input(id='input-2-state', type='text', value=data['country']),
#             html.Button(id='submit-button', n_clicks=0, children='Submit')
#         ])
#     )
    
# def finalize(app, data, fl):
    
#     # example callback that updates client side data
#     @app.callback(Output('output-form-n-clicks', 'children'),
#                   [Input('submit-button', 'n_clicks')])
#     def callback(n_clicks):
#         return json.dumps({ 'n_clicks': n_clicks })
    








from dash.dependencies import Input, Output
from blocks.example_blocks import InputForm
import json

def layout(app, data, fl):
    
    input_form = InputForm(app, data)
    fl.register_vis('InputForm', input_form.layout)
    fl.blocks.register('InputForm', input_form)
    
    fl.register_data('output-form-n-clicks', { 'n_clicks': 0 })
    fl.register_data('for-fun', { 'hi': 'hello' })
    
    @app.callback(Output('output-form-n-clicks', 'children'),
                  [input_form.input('submit-button', 'n_clicks')])
    def callback(n_clicks):
        return json.dumps({ 'n_clicks': n_clicks })
    
def finalize(app, data, fl):
    pass