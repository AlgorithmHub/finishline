import dash_html_components as html
import importlib.util
import glob
import os.path
import sys
import traceback

import finishline.grid_components as gc

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import random
import json
from dash.exceptions import PreventUpdate



class FinishLine(object):
    
    def __init__(
            self, 
            app=None,
            data=None,
            show_data=True,
            on_layout_change=None):

        self.name = 'default'
        
        # server side
        self.app = app or dash.Dash()
        self.data = data or {}
        self.plugins = {}
        self.blocks = BlockManager()
        
        # client side
        self.client_vis  = {}
        self.client_data = {}
        
        # misc
        self.extra_files = []
        self.show_data = show_data
        
        # callbacks
        self.on_layout_change = on_layout_change or (lambda lo: print('layout', lo)) 
        
        
    def register_vis(self, name, layout):
                
        self.client_vis[name] = layout
        

    def register_data(self, name, data=None, callback=None):
        
        self.client_data[name] = data or {}
        
        if callback:
            @self.app.callback(Output(name, 'role'),
                              [Input(name, 'children')])
            def data_callback(new_data):
                callback(json.loads(new_data))
                raise PreventUpdate()
                
        
    def generate_layout(self, components=gc, layouts={}):
        
        page_id = self.name + '-fl-page'
        
        page_layout = page_id + '-layout'
        page_config = page_id + '-config'
        page_data   = page_id + '-data'
        
        # register page configuration
        self.register_data(page_config, layouts, self.on_layout_change)
        
        # push fl-page-config to data
        @self.app.callback(Output(page_config, 'children'),
                          [Input(page_layout, 'layouts')])
        def get_layout(new_config):
            return json.dumps(new_config)
                
        # client side data objects
        c_data_style = {'display':'block'} if self.show_data else {'display':'none'}
        c_data = [html.Div(json.dumps(v), id=k) for k,v in self.client_data.items()]
                
        # client side visualization objects
        c_vis = self._gen_c_vis(components, layouts)

        self.finalize()
        return components.Page(
            [components.Layout(c_vis, id=page_layout, layouts=layouts),
             html.Div(c_data, className='fl-data', id=page_data, style=c_data_style)],
            id=page_id)
    
    
    def _gen_c_vis(self, components, layouts):
        
        ks,vs = zip(*self.client_vis.items())
        # TODO not obvious that 'lg' needs to be defined and i needs to be an index
        return [components.Card(vs[int(ci['i'])], title=ks[int(ci['i'])], i=ci['i']) for ci in layouts['lg']]
                
    
    def load_plugins(self, plugins_path='plugins/*'):
        
        modules = sorted(glob.glob(plugins_path))

        for m in modules:
            print(m)
            fname = m + '/__init__.py'
            if not os.path.isfile(fname):
                continue
            self.extra_files.append(fname) #TODO walk all py files in dir
            spec = importlib.util.spec_from_file_location(m, fname)
            print(spec)
            plugin = importlib.util.module_from_spec(spec)
            
            try:
                spec.loader.exec_module(plugin)
                plugin.layout(self.app, self.data, self)
            except:
                traceback.print_exc()
                print("Unexpected error in plugin, ", m, ": ", sys.exc_info()[0])
                self.register_vis(m, html.Pre("Unexpected error in " + m + '\n' + traceback.format_exc()));
                
            self.plugins[m] = plugin
             
                
    def finalize(self):
        for plugin in self.plugins.values():
            if 'finalize' in plugin.__dict__:
                plugin.finalize(self.app, self.data, self)
    
    
    def run_server(self,
                   port=5000,
                   debug=False,
                   **flask_run_options):
        self.app.run_server(port=port, debug=debug, extra_files=self.extra_files, **flask_run_options)
                
                
class BlockManager:
    
    def __init__(self):
        
        self._blocks = {}
        
        
    def register(self, name, block):
        
        self._blocks[name] = block
        
        
    def __getitem__(self, name):
        print(self._blocks.keys())
        return self._blocks[name]
