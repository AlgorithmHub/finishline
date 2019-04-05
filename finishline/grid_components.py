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


def Layout(children=None, layouts=None, cols=None, rowHeight=300, **kwargs):
    
    layouts = layouts or {'lg':[], 'md':[], 'sm':[] }
    cols = cols or { 'lg': 3, 'md': 2, 'sm': 1 }
    
    return dgl.ResponsiveGridLayout(
        children,
        layouts=layouts,
        cols=cols,
        rowHeight=rowHeight,
        draggableHandle='.fl-titlebar',
        verticalCompact=True,
        **kwargs
    )


def Card(children, title='Undefined', i=0, href=None, **kwargs):
    
    t = html.A(title, href=href, target=title) if href is not None else title
    if isinstance(children, dcc.Graph):
        # note: don't put children in a div container wrapper, else plotly won't resize properly
        c = [html.Div(t, className='fl-titlebar')] + [children]
    else:
        c = [html.Div(t, className='fl-titlebar'), html.Div(children, className='fl-content')]
        

    return html.Div(
        c,
        className='fl-card',
        key=str(i),
        id=str(i),
        style=merge({}, kwargs.get('style', {})),
        **omit(['style'], kwargs)
    )