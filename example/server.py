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
        {"w": 2, "h": 1, "x": 1, "y": 2, "i": ".$plugins/ErrorBlock"}, 
        {"w": 2, "h": 2, "x": 0, "y": 0, "i": ".$HelloWorld"}, 
        {"w": 1, "h": 1, "x": 2, "y": 0, "i": ".$InputForm"}, 
        {"w": 1, "h": 1, "x": 2, "y": 1, "i": ".$OutputForm"}, 
        {"w": 1, "h": 1, "x": 0, "y": 2, "i": ".$Test Layout"}
    ],

})

if __name__ == '__main__':
    fl.run_server(debug=True, port=5000, host='0.0.0.0')
