import dash
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly as py
import plotly.graph_objs as go
import json
import random
import os
from Algorithms import dictionary_dimension_conversion
from datetime import datetime
################################################################################################################################################################


Graph1 = "country_by_revenue.json"
Graph2 = "product_type_by_revenue.json"
Graph3 = "product_type_by_channel_and_profit.json"
Graph4 = "country_by_product_cost1.json"
Graph5 = "product_type_by_cost.json"
Graph6 = "product_type_by_channel_and_cost.json"
Graph7 = "social_media_comments.json"
Graph8 = "social_media_comments_by_product_line.json"
countries = "countries.json"
################################################################################################################################################################


with open(countries, "r") as file:
    countries_data = json.load(file)
with open (Graph1, "r") as file:
    Graph1_Data = json.load(file)
with open (Graph2, "r") as file:
    Graph2_Data = json.load(file)
with open (Graph3, "r") as file:
    Graph3_Data = json.load(file)
with open (Graph4, "r") as file:
    Graph4_Data = json.load(file)
with open (Graph5, "r") as file:
    Graph5_Data = json.load(file)
with open (Graph6, "r") as file:
    Graph6_Data = json.load(file)
with open (Graph7, "r") as file:
    Graph7_Data = json.load(file)
with open (Graph8, "r") as file:
    Graph8_Data = json.load(file)
################################################################################################################################################################


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
server = app.server
app.title = "Data Dashboard"

styles = {
    'pre': {
        'border': 'thick grey solid',
        'overflowX': 'scroll',
    }
}
################################################################################################################################################################

################################################################################################################################################################
card1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/revenue.png", top=True),
        dbc.CardBody
        (
            [
                html.H2("Total Revenue and Product Cost per Country", className="card-title"),
                dbc.Button("View Graph", color="primary", id="open-modal1"),
                dbc.Modal
                (
                    [
                        dbc.ModalHeader("Header"),
                        dbc.ModalBody(
                            children=[
                                dbc.Row(dbc.Col(
                                        children=[
                                            dcc.Dropdown(
                                                id="modal1-dropdown",
                                                options=[
                                                    {"label": "Revenue per Country", "value":"Revenue"},
                                                    {"label": "Product Cost per Country", "value":"Product Cost"},
                                                ],
                                                value="Revenue"
                                            )
                                        ]
                                    )),
                                    dbc.Row(
                                        children=[
                                            dbc.Col(
                                                id="graph1-geo1", 
                                                children=[
                                                    dcc.Graph(id='graph1'), 
                                                    dcc.Interval(id="update-graph1", interval=1000)
                                                ]
                                            )
                                        ]
                                    )
                            ]
                        ),
                        dbc.ModalFooter(dbc.Button("Close", color="primary", id="close-modal1", className="ml-auto"))
                    ],
                    id="modal1",
                    size="xl",
                    centered = True
                )
            ]
        )
    ]
)

@app.callback(Output('graph1', 'figure'), [Input('update-graph1', 'n_intervals'), Input("modal1-dropdown", "value")])
def update_graph1(input_data, dropdown_value):
    if dropdown_value == "Revenue":
        data_values = Graph1_Data.get("Revenue Values")
    else:
        data_values = Graph4_Data.get("Product Cost Values")

    for i in range(len(data_values)):
        random_num = random.uniform(0.8, 1.2)
        data_values[i] = random_num * data_values[i]

    data = go.Scattergeo(
        name=dropdown_value,
        showlegend=True,
        mode="markers",
        lat= Graph1_Data.get("Latitude"),
        lon= Graph1_Data.get("Longitude"),
        text= data_values,
        hovertext= Graph1_Data.get("Countries"),
        hovertemplate= f"{dropdown_value}" + ': $%{text: .0f}<br>Country: %{hovertext}',
        marker= dict(
            opacity=1,
            size= data_values,
            sizeref=1000,
            sizemin=1,
            sizemode="area",
            gradient = dict(
                type="radial",
                color="red"
            ),
            color = "blue"
        )
    )
    layout = {
        "geo": {
            "scope": "world", 
            "showframe": True, 
            "projection": {"type": "hide"},  #miller, orthographic, hide
            "showcountries": False, 
            "showcoastlines": True
        },
        "title": "Sum of " + dropdown_value + " per Country (USD)",
        "hovermode": "closest",
        "margin": {'l': 80, 'r': 0, 'b': 0, 't': 50},
        "clickmode": "event+select"
    }
    return {"data": [data], "layout": layout}


@app.callback(
    Output("modal1", "is_open"),
    [Input("open-modal1", "n_clicks"), Input("close-modal1", "n_clicks")],
    [State("modal1", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
################################################################################################################################################################


row1 = dbc.Row(
    [
        dbc.Col(id="card1", children=[card1], width=4)
    ]
)
app.layout = html.Div([row1])

if __name__ == "__main__":
    app.run_server(debug=True)