# import sys
# sys.path.append('..')

import dash
from finishline import FinishLine

app = dash.Dash()
app.config.supress_callback_exceptions = True
app.scripts.config.serve_locally = True

data = { 'state': 'Montréal', 'country': "Canada" }

fl = FinishLine(app=app, 
                data=data, 
                debug=True, 
                debug_path={'root':'/workspace/', 'target':'/jupyter/edit/'})
fl.load_plugins()
app.layout = fl.generate_layout(layouts={
    'lg':[
      {'i': '1', 'x': 0, 'y': 0, 'w': 2, 'h': 2},
      {'i': '2', 'x': 2, 'y': 0, 'w': 1, 'h': 1},
      {'i': '3', 'x': 2, 'y': 1, 'w': 1, 'h': 1},
      {'i': '0', 'x': 0, 'y': 2, 'w': 2, 'h': 1},
      {'i': '4', 'x': 2, 'y': 2, 'w': 1, 'h': 1},
    ],
    'md':[],
    'sm':[]
})

if __name__ == '__main__':
    fl.run_server(debug=True, port=5000, host='0.0.0.0')
