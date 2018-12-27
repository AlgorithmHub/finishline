===========
Finish Line
===========

Finish Line is a framework for quickly building beautiful customizable dashboards in Plotly Dash.
The framework provides utility for developers to easily plugin new interactive visualization
components into the dashboard. Components are automatically added to the dashboard using a responsive
grid layout.

----------------------
How to use Finish Line
----------------------

An example use of the framework is located in the GitHub repo under the ``example`` directory. The
following shows the minimum code required to start a Finish Line dashboard server.

.. code:: python

    from finishline import FinishLine
    import dash

    app = dash.Dash()
    data = load_my_data()

    fl = FinishLine(app=app, data=data)
    fl.load_plugins()
    app.layout = fl.generate_layout()

    if __name__ == '__main__':
        fl.run_server(debug=True, port=5000, host='0.0.0.0')
        
Visualization components are loaded from the ``plugins`` folder. The default location is in a folder
called ``plugins`` in the current working directory (directory the web server is started). Individual
plugins are located in subfolders under the ``plugins`` folder. The entry point to a plugin is in the
file ``__init__.py``.

Here is an example component. The code is placed in ``./plugins/HelloWorld/__init__.py``

.. code:: python

    import dash_html_components as html
    import dash_core_components as dcc

    def initialize(app, data, fl):

        fl.register_vis(
            'HelloWorld',
            dcc.Graph(
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
        )
        
    def finalize(app, data, fl):
        pass


------------
Installation
------------

Finish Line depends upon ``dash``. Note, we have only tested with ``python3``.

Requirements:

* dash
* dash-responsive-grid-layout

**Install Options**

.. code:: bash

    pip3 install finishline


------------
Build
------------

**Create distribution**

* edit setup.py and change version number

.. code:: bash

    python3 setup.py sdist bdist_wheel

**Install distribution locally**

.. code:: bash

    pip3 uninstall finishline
    pip3 install dist/finishline-VERSION-py3-none-any.whl

**Push to test pip**

.. code:: bash

    twine upload --repository-url https://test.pypi.org/legacy/ dist/*VERSION*
    pip3 install -U --index-url https://test.pypi.org/simple/ finishline

**Push to production pip**

.. code:: bash

    twine upload dist/*VERSION*
    pip3 install -U finishline


--------
Features
--------

* Client and server side data store API
* Plugin visualization component API
* Responsive grid layout
* Customizable grid layout via drag and drop
* Developer mode

----------
To Do List
----------

* Save layout
* Reusable components API
* Hide/Show components
* Support multiple pages
* Better support for resizing plotly charts
