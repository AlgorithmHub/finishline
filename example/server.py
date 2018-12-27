import sys
sys.path.append('..') # comment out if importing from pip module

import dash
from finishline import FinishLine

app = dash.Dash()
app.config.supress_callback_exceptions = True
app.scripts.config.serve_locally = True
app.title = 'Dash FinishLine'

data = { 'state': 'Montréal', 'country': "Canada" }

fl = FinishLine(app=app, 
                data=data, 
                debug=True, 
                debug_path={'root':'/workspace/', 'target':'/jupyter/edit/'})
fl.load_plugins()
app.layout = fl.generate_layout(layouts={
    'lg':[
      {'i': 'HelloWorld',         'x': 0, 'y': 0, 'w': 2, 'h': 2},
      {'i': 'InputForm',          'x': 2, 'y': 0, 'w': 1, 'h': 1},
      {'i': 'OutputForm',         'x': 2, 'y': 1, 'w': 1, 'h': 1},
      {'i': 'plugins/ErrorBlock', 'x': 0, 'y': 2, 'w': 2, 'h': 1},
      {'i': 'Test Layout',        'x': 2, 'y': 2, 'w': 1, 'h': 1},
    ],
    'md':[],
    'sm':[]
})

if __name__ == '__main__':
    fl.run_server(debug=True, port=5000, host='0.0.0.0')
