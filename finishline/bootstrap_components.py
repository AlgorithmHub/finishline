# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent


def merge(a, b):
    return dict(a, **b)


def omit(omitted_keys, d):
    return {k: v for k, v in d.items() if k not in omitted_keys}


def Page(children=None, **kwargs):
    return html.Div(
        children,
        className='container-width',
        **kwargs
    )


def Layout(children=None, layouts=None, cols=None, rowHeight=300, **kwargs):    
    return html.Div(
        children,
        className="row",
        style={
            'padding': 10,
        },
        **kwargs
    )


def Card(children, title='Undefined', i=0, href=None, width=6, **kwargs):

    t = html.A(title, href=href, target=title) if href is not None else title
    c = [html.Div(t, className='fl-titlebar'), html.Div(children, style={'padding': 20 })]

    return html.Div(
        c,
        className='fl-card col-sm-{}'.format(str(width)),
        style=merge({
            'padding': 20,
            'margin': 0,
        }, kwargs.get('style', {})),
        **omit(['style'], kwargs)
    )