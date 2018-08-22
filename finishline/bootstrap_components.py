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


def Layout(children=None, layouts=None, **kwargs):    
    return html.Div(
        children,
        className="row",
        style={
            'padding': 10,
        },
        **kwargs
    )


def Card(children, title='Undefined', i=0, width=6, **kwargs):

    number_mapping = {
        1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9', 10: '10', 11: '11',
        12: '12'
    }
    
    c = [html.Div(title, className='fl-titlebar'), html.Div(children, style={'padding': 20 })]

    return html.Div(
        c,
        className='fl-card col-sm-{}'.format(number_mapping[width]),
        style=merge({
            'padding': 20,
            'margin': 0,
        }, kwargs.get('style', {})),
        **omit(['style'], kwargs)
    )