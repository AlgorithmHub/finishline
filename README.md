# Dash Finish Line

```
git clone https://github.com/AlgorithmHub/finishline.git
cd finishline/example
pip3 install dash dash-responsive-grid-layout
python3 server.py
```

To create a new viz block:

```
cd finishline/example
cp -r plugins/HelloWorld plugins/MyNewBlock
vi plugins/MyNewBlock
```

Features:

* Component plugin interface
* Data store API
* Visualiztion API
* Responsive grid layout compatible with plotly
* Dynaimc grid layout

Things to do:

* Save layout
* Finish reusable components API
* Allow layout to add missing components
* Hide/Show components
* Multiple page layout
* ...
