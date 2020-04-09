import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Img(
        id='display_pic',
        src=app.get_asset_url('cinema.png')
    ),
    
    dcc.RadioItems(
        id='form_buttons',
        options=[
            {'label': 'Tablet', 'value': 'T'},
            {'label': 'Desktop', 'value': 'D'},
            {'label': 'TableTop', 'value': 'SF'},
            {'label': 'HomeCinema', 'value': 'HC'},
            {'label': 'Cinema', 'value': 'C'}
        ],
        value='Display Form Factor',
        labelStyle={'display': 'inline-block'}
    )   
 
  
])


@app.callback(
    Output(component_id='display_pic', component_property='src'),
    [Input(component_id='form_buttons', component_property='value')]
)
def update_image(button_value):
    if button_value=='C':
        src=app.get_asset_url('cinema.png')
        return src
    else:
        src=app.get_asset_url('tablet.png')
        return src 



if __name__ == '__main__':
    app.run_server(debug=True)