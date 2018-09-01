import dash_html_components as html

def initialize(app, data, fl):
    fl.register_vis('Error Block', html.Div([
        html.H1('This Block has a Syntax Error')
    ])))
