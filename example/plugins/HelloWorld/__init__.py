from dash.dependencies import Output, Input, State
import dash_html_components as html
import dash_core_components as dcc
<<<<<<< HEAD
import dash_building_blocks as dbb
import json
    
    
class HelloWorld(dbb.Block):
    
    def layout(self):
        return dcc.Graph(
=======

def initialize(app, data, fl):

    fl.register_vis('HelloWorld',
        dcc.Graph(
>>>>>>> master
            id='basic-chart',
            figure={
                'data': [
                    {
                        'x': [1, 2, 3, 4],
                        'y': [4, 1, 3, 5],
                        'text': ['a', 'b', 'c', 'd'],
                        'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                        'name': 'Trace 1',
                        'mode': 'markers',
                        'marker': {'size': 12}
                        },
                    {
                        'x': [1, 2, 3, 4],
                        'y': [9, 4, 1, 4],
                        'text': ['w', 'x', 'y', 'z'],
                        'customdata': ['c.w', 'c.x', 'c.y', 'c.z'],
                        'name': 'Trace 2',
                        'mode': 'markers',
                        'marker': {'size': 12}
                        }
                    ]
                },
            config={
                'autosizable': True
                }
            )
            

def initialize(app, data, fl):
    
    hello_world = HelloWorld(app, data)
    fl.register_vis('HelloWorld', hello_world.layout)
    

def finalize(app, data, fl):
    pass