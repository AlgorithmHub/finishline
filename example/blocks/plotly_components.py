# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent


def merge(a, b):
    return dict(a, **b)


def omit(omitted_keys, d):
    return {k: v for k, v in d.items() if k not in omitted_keys}


def Header(title):
    return html.Div(
        style={'borderBottom': 'thin lightgrey solid', 'marginRight': 20},
        children=[html.Div(title, style={'fontSize': 30})]
    )


def Row(children=None, **kwargs):
    return html.Div(
        children,
        className="row",
        **kwargs
    )


def Column(children=None, width=1, **kwargs):
    number_mapping = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
        12: 'twelve'
    }
    return html.Section(
        children,
        className="{} columns".format(number_mapping[width]),
        **kwargs
    )


def ControlPanel(children=None, **kwargs):
    return Card(
        children,
        style={
            'marginTop': 20,
            'marginBottom': 0,
            'marginLeft': 0,
            'marginRight': 0,
            'padding': 10
        }
    )


def Card(children, **kwargs):
    return html.Section(
        children,
        style=merge({
            'padding': 20,
            'margin': 20,
            'borderRadius': 5,
            'border': 'thin lightgrey solid',
            'overflow-x': 'scroll'
        }, kwargs.get('style', {})),
        **omit(['style'], kwargs)
    )


def GraphCard(title=None, **kwargs):

    if title is not None:
        card = Card(
                    children=[
                        html.Div(
                            html.B(title),
                            style={'borderBottom': 'thin lightgrey solid'}),
                        dcc.Graph(
                            **kwargs
                        )
                    ]
                )
    else:
        card = Card(
                    children=[
                        dcc.Graph(
                            **kwargs
                        )
                    ]
                )
    return card


def TopicCard(markup, table, **kwargs):

    card = Card(
                [
                    dcc.Markdown(
                        dedent(markup),
                        **omit(['style'], kwargs)
                    ),
                    table
                ]
            )
    return card


def Comment(children, **kwargs):
    return Card(
        children=dcc.Markdown(
            dedent(children),
            **omit(['style'], kwargs)
        )
    )
