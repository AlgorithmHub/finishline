import importlib.util
import glob
import os.path
import sys
import traceback

import finishline.grid_components as gc

import dash

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_building_blocks as dbb
import random
import json
from dash.exceptions import PreventUpdate



class FinishLine(object):
    
    def __init__(
            self, 
            app=None,
            data=None,
            name='default',
            debug=False,
            on_layout_change=None,
            debug_path=None):

        self.name = name
        
        # server side
        self.app = app or dash.Dash()
        self.data = data or {}
        self.plugins = {}
        self.blocks = BlockManager()
        self.store = FinishStore(app, hide=(not debug))
        
        # client side
        self.client_vis  = {}
        self.client_data = {}
        
        # misc
        self.extra_files = []
        self.debug = debug
        self.debug_path = debug_path
        
        #private
        self._curr_file = None
        
        
        
        # callbacks
        self.on_layout_change = on_layout_change or (lambda lo: print('layout', lo)) 
        
        
    def register_vis(self, name, layout):
                
        self.client_vis[name] = {
            'layout': layout,
            'src_file': self._curr_file
        }
        

    def register_data(self, name, inputs=None, state=None, data=None, on_update=None):
        
        self.client_data[name] = {
            'data': data or {},
            'src_file': self._curr_file
        }
                
        ret = self.store.register(name, inputs=inputs, state=state, initially=data)
        
        if on_update:
            @self.app.callback(
                Output(self.store.ids[name], 'role'),
                [self.store.input(name)]
            )
            def data_callback(new_data):
                on_update(json.loads(new_data))
                raise PreventUpdate()
        
        return ret
                
        
    def generate_layout(self, components=gc, layouts=None, cols=None):
        
        page_id = self.name + '-fl-page'
        
        page_layout = page_id + '-layout'
        page_config = page_id + '-config'
        page_data   = page_id + '-data'
        
        @self.register_data(
            page_config, 
            inputs=[Input(page_layout, 'layouts')],
            data=layouts,
            on_update=self.on_layout_change
        )
        def get_layout(new_config):
            return json.dumps(new_config)
                
        # client side data objects
        c_data_style = {'display':'block'} if self.debug_path else {'display':'none'}
        c_data = self.store.debug_layout(self.client_data)
                
        # client side visualization objects
        c_vis = self._gen_c_vis(components, layouts)
        layout = components.Page(
            [components.Layout(c_vis, id=page_layout, layouts=layouts, cols=cols), 
             html.Div(c_data, className='fl-data', id=page_data, style=c_data_style)],
            id=page_id)

        # run plugin finalize method, e.g. should be used to create callbacks
        self._finalize()
        
        return layout
    
    
    def _gen_c_vis(self, components, layouts):
        i = 0
        c = []
        ii = [l['i'] for l in layouts['lg']] if (layouts and 'lg' in layouts) else []
        for (name, vis) in self.client_vis.items():
            key = str(i) if str(i) in ii else name
            key = name if name in ii else key
            c.append(components.Card(vis['layout'], title=name, i=key, href=vis['src_file']))
            i = i + 1
            
        return c
                
    
    def load_plugins(self, plugins_path='plugins/*'):
        
        modules = sorted(glob.glob(plugins_path))

        for m in modules:
#             print(m)
            fname = m + '/__init__.py'
            if not os.path.isfile(fname):
                continue
            
            if self.debug_path is not None:
                self._curr_file = os.path.abspath(fname).replace(self.debug_path['root'], self.debug_path['target'])
            
            self.extra_files.append(fname) #TODO walk all py files in dir
            spec = importlib.util.spec_from_file_location(m, fname)
#             print(spec)
            plugin = importlib.util.module_from_spec(spec)
            
            try:
                spec.loader.exec_module(plugin)
                plugin.initialize(self.app, self.data, self)
            except:
                traceback.print_exc()
                print("Unexpected error in plugin, ", m, ": ", sys.exc_info()[0])
                self.register_vis(m, html.Pre("Unexpected error in " + m + '\n' + traceback.format_exc()))
                # TODO: register 'XXX' instead of 'plugin/XXX'
                
            self.plugins[m] = plugin
             
                
    def _finalize(self):
        for plugin in self.plugins.values():
            if 'finalize' in plugin.__dict__:
                plugin.finalize(self.app, self.data, self)
    
    
    def run_server(self,
                   port=5000,
                   debug=False,
                   **flask_run_options):
        self.app.run_server(port=port, debug=debug, extra_files=self.extra_files, **flask_run_options)


class FinishStore(dbb.Store):
    
    def debug_layout(self, client_data):
        style = {'display': 'none'} if self.hide else None
        return html.Div([
            html.Div([html.A(children=[k+':'],href=v['src_file'],target=k), html.Div(json.dumps(v['data']), id=self.ids[k])])
            for k, v in client_data.items()
        ])
        
    
class BlockManager:
    
    def __init__(self):
        
        self._blocks = {}
        
        
    def register(self, name, block):
        
        self._blocks[name] = block
        
        
    def __getitem__(self, name):
        
        return self._blocks[name]
        
        
    def __getattr__(self, name):
        
        return self._blocks[name]
