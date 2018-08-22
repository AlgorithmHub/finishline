import dash_html_components as html
from blocks.example_blocks import OutputForm
    
def layout(app, data, fl):
    output_form = OutputForm(app, data)
    
    fl.register_vis('OutputForm', output_form.layout)
    fl.blocks.register('OutputForm', output_form)
    
def finalize(app, data, fl):
    output_form = fl.blocks['OutputForm']
    output_form.resolve({
        'n_clicks': fl.blocks['InputForm']['submit-button']['n_clicks'],
        'input1': fl.blocks['InputForm']['input-1-state']['value'],
        'input2': fl.blocks['InputForm']['input-2-state']['value'],
    })
