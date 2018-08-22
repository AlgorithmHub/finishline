# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent

import dash_responsive_grid_layout as dgl
import copy

def merge(a, b):
    return dict(a, **b)


def omit(omitted_keys, d):
    return {k: v for k, v in d.items() if k not in omitted_keys}


def Page(children=None, **kwargs):
    return html.Div(
        children,
        className='fl-page',
        **kwargs
    )


def Layout(children=None, layouts={'lg':[], 'md':[], 'sm':[] }, **kwargs):
    
    return dgl.ResponsiveGridLayout(
        children,
        cols={ 'lg': 3, 'md': 2, 'sm': 1 },
        rowHeight=300,
        layouts=layouts,
        draggableHandle='.fl-titlebar',
        **kwargs
    )


def Card(children, title='Undefined', i=0, **kwargs):
    
    # note: don't put children in a div container wrapper, else plotly won't resize properly
    #c = [html.Div(title, className='fl-titlebar'), html.Div(children, className='fl-content')]
    c = [html.Div(title, className='fl-titlebar')] + [children]

    return html.Div(
        c,
        className='fl-card',
        key=str(i), #TODO made this interface better (i.e. allow for arbitrary key assignment)
        style=merge({}, kwargs.get('style', {})),
        **omit(['style'], kwargs)
    )