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
        'overflow': 'scroll',
    }
}
################################################################################################################################################################
cheating_button = html.Div(
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Button("Click to view decision based on previous experience", id="open-cheating-modal", size="lg", color="primary", disabled=False),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Decision"),
                            dbc.ModalBody(
                                html.H3("Retail Shorts USA")
                            ),
                            dbc.ModalFooter(dbc.Button("Close", id="close-cheating-modal"))
                        ],
                        id="cheating-modal",
                        size="lg",
                        centered=True
                    )
                ]
            )
        ]
    )
)

'''
@app.callback(
    [#Output("open-cheating-modal", "disabled"),
    Output("open-modal1", "disabled"),
    Output("open-modal2", "disabled"),
    Output("open-modal3", "disabled"),
    #Output("open-modal4", "disabled"),
    #Output("open-modal5", "disabled"),
    Output("open-modal6", "disabled"),
    Output("open-modal7", "disabled"),
    Output("open-modal8", "disabled"),
    Output('completed-analysis-modal-button', "disabled"),
    Output('start-analysis-button', "disabled")],
    [Input("start-analysis-button", "n_clicks"),
    Input("completed-analysis-modal-button", "n_clicks")]
)
def activate_buttons(start_click, end_click):
    if start_click == None and end_click == None:
        return [True, True, True, True, True, True, True, True, False]
    elif start_click != None and end_click == None:
        return [False, False, False, False, False, False, False, False, True]
    else:
        return [True]*9
'''
@app.callback(Output("completed-analysis-modal", "is_open"), [Input("completed-analysis-modal-button", "n_clicks"), Input("close-completed-analysis-modal", "n_clicks")], [State("completed-analysis-modal", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("cheating-modal", "is_open"), [Input("open-cheating-modal", "n_clicks"), Input("close-cheating-modal", "n_clicks")], [State("cheating-modal", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("token", "children"),
    [
        Input("completed-analysis-modal-button", "n_clicks"),
        Input("open-cheating-modal", "n_clicks"),
        Input("open-modal1", "n_clicks_timestamp"),
        Input("open-modal2", "n_clicks"),
        Input("open-modal3", "n_clicks"),
        #Input("open-modal4", "n_clicks"),
        #Input("open-modal5", "n_clicks"),
        Input("open-modal6", "n_clicks"),
        Input("open-modal7", "n_clicks"),
        Input("open-modal8", "n_clicks"),
        Input("completed-analysis-modal-button", "n_clicks_timestamp"),
        Input("start-analysis-button", "n_clicks_timestamp"),
    ]
)
def tokens(a,b,c,d,e,f,g,h,i,j):
    answer = [a,b,c,d,e,f,g,h]
    summation = [x+1 for x in range(len(answer)) if answer[x] != None]
    token = 0
    for x in summation:
        token = token*10 + x
    
    if i != None and j != None:
        difference = i - j
        return str(token) + "a" + str(difference//1000) + "a"
    else:
        return str(token)
################################################################################################################################################################

################################################################################################################################################################
card1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/revenue.png", top=True),
        dbc.CardBody
        (
            [
                html.Br(),
                html.Br(),
                html.H2("Total Revenue and Product Cost per Country", className="card-title"),
                dbc.Button("View Graph", color="primary", id="open-modal1", disabled=False),
                dbc.Modal
                (
                    [
                        dbc.ModalHeader("Header"),
                        dbc.ModalBody(
                            children=[    
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            id="graph1-geo1", 
                                            children=[
                                                dcc.Graph(id='graph1'), 
                                                dcc.Interval(id="update-graph1", interval=10000)
                                            ]
                                        ),
                                        dbc.Col(
                                            id="graph4-geo2",
                                            children=[
                                                dcc.Graph(id='graph4'), 
                                                dcc.Interval(id="update-graph4", interval=10000)
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

@app.callback(Output('graph1', 'figure'), [Input('update-graph1', 'n_intervals')])
def update_graph1(input_data):
    data_values = Graph1_Data.get("Revenue Values")

    for i in range(len(data_values)):
        random_num = random.uniform(0.8, 1.2)
        data_values[i] = random_num * data_values[i]

    data = go.Scattergeo(
        name="Revenue",
        showlegend=True,
        mode="markers",
        lat= Graph1_Data.get("Latitude"),
        lon= Graph1_Data.get("Longitude"),
        text= data_values,
        hovertext= Graph1_Data.get("Countries"),
        hovertemplate= "Revenue: $%{text: .0f}<br>Country: %{hovertext}",
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
            "projection": {"type": "orthographic"},  #miller, orthographic, hide
            "showcountries": False, 
            "showcoastlines": True
        },
        "title": "Sum of Revenue per Country (USD)",
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


@app.callback( Output("modal4", "is_open"), [Input("open-modal4", "n_clicks"), Input("close-modal4", "n_clicks")], [State("modal4", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output('graph4', 'figure'), [Input('update-graph4', 'n_intervals')])
def update_graph4(input_data):
    data = go.Scattergeo(
        name="Product Cost",
        showlegend=True,
        mode="markers",
        lat= Graph4_Data.get("Latitude"),
        lon= Graph4_Data.get("Longitude"),
        text= Graph4_Data.get("Product Cost Values"),
        hovertext= Graph4_Data.get("Countries"),
        hovertemplate= "Product Cost: $%{text: .0f}<br>Country: %{hovertext}",
        marker= dict(
            opacity=1,
            size=Graph4_Data.get("Product Cost Values"),
            sizeref=1000,
            sizemin=1,
            sizemode="area",
            gradient = dict (
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
            "projection": {"type": "orthographic"},  #miller, orthographic, hide
            "showcountries": False, 
            "showcoastlines": True
        }, 
        "title": "Sum of Product Cost per Country (USD)",
        "hovermode": "closest",
        "margin": {'l': 80, 'r': 0, 'b': 0, 't': 50},
        "clickmode": "event+select"
    }
    return {"data": [data], "layout": layout}
################################################################################################################################################################
card3 = dbc.Card(
    [
        dbc.CardImg(src="/assets/pie.png", top=True),
        dbc.CardBody(
            [
                html.Br(),
                html.H2("Total Revenue per Product Line", className="card-title"),
                dbc.Button("View Graph", color="primary", id="open-modal2", disabled=False),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Header"),
                        dbc.ModalBody(dbc.Row(dbc.Col([dcc.Graph("graph2"), dcc.Interval("update-graph2")]))),
                        dbc.ModalFooter(dbc.Button("Close", size="md", color="primary", id="close-modal2"))
                    ],
                    id="modal2",
                    size="lg",
                    centered=True
                )
            ]
        ),
    ]
)

@app.callback( Output("modal2", "is_open"), [Input("open-modal2", "n_clicks"), Input("close-modal2", "n_clicks")], [State("modal2", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output('graph2', 'figure'), [Input('update-graph2', 'n_intervals')])
def update_graph2(input_data):
    x_values = list(Graph2_Data.keys())
    y_values = list(Graph2_Data.values())

    for i in range(len(y_values)):
        random_num = random.uniform(0.9, 1.1)
        y_values[i] = int(y_values[i] * random_num)
    
    data = go.Pie(
        labels = x_values,
        values = y_values,
        hoverinfo = 'label+percent+value',
        #hovertemplate= 'Cost: $%{y_values}<br>Product Line: %{hovertext}'
    )

    layout = {
        "title": "Sum of Revenue per Product Line (USD)",
        "clickmode": "event+select"
    }

    return {"data": [data], "layout": layout}
################################################################################################################################################################


card4 = dbc.Card(
    [
        html.Br(),
        dbc.CardImg(src="/assets/multiHBar.png", top=True),
        dbc.CardBody(
            [
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H2("Total Product Cost per Channel", className="card-title"),
                dbc.Button("View Graph", color="primary", id="open-modal6", disabled=False),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Header"),
                        dbc.ModalBody(dbc.Row(dbc.Col([dcc.Graph(id="graph6"), dcc.Interval(id="update-graph6", interval=1000)]))),
                        dbc.ModalFooter(dbc.Button("Close", id="close-modal6", color="primary", size="md"))
                    ],
                    id="modal6",
                    size="lg",
                    centered=True
                )
            ]
        ),
    ]
)

@app.callback( Output("modal6", "is_open"), [Input("open-modal6", "n_clicks"), Input("close-modal6", "n_clicks")], [State("modal6", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("graph6", "figure"), [Input("update-graph6", "n_intervals")])
def update_graph6(input_data):
    x_values = list(Graph6_Data.get("Direct Marketing").keys())
    direct_marketing = list(Graph6_Data.get("Direct Marketing").values())
    ecommerce = list(Graph6_Data.get("Ecommerce").values())
    retail = list(Graph6_Data.get("Retail").values())
    product_cost = list(Graph5_Data.values())

    for i in range(len(x_values)):
        random_num_dm = random.uniform(0.9, 1.1)
        random_num_em = random.uniform(0.9, 1.1)
        random_num_rt = random.uniform(0.9, 1.1)
        random_num_pc = random.uniform(0.9, 1.1)
        direct_marketing[i] = direct_marketing[i] * random_num_dm
        ecommerce[i] = ecommerce[i] * random_num_em
        retail[i] = retail[i] * random_num_rt
        product_cost[i] = product_cost[i] * random_num_pc

    data_dm = go.Bar(
        y = x_values,
        x = direct_marketing,
        name="Direct Marketing",
        orientation= "h"
    )
    data_em = go.Bar(
        y= x_values,
        x= ecommerce,
        name="Ecommerce",
        orientation= "h"
    )
    data_rt = go.Bar(
        y= x_values,
        x= retail,
        name= "Retail",
        orientation= "h"
    )
    data_pc = go.Bar(
        y= x_values,
        x= product_cost,
        name= "Total Channel Product Cost",
        orientation= "h"
    )

    layout = {
        "title": "Sum of Product Cost per Product Line per Channel (USD)",
        "barmode": "group",
        "bargap": 0.5,
        "xaxis_title": "Product Per Channel",
        "yaxis_title": "Cost in USD",
        "clickmode": "event+select"
    }

    return {"data": [data_dm, data_rt, data_em, data_pc], "layout": layout}
################################################################################################################################################################


card5 = dbc.Card(
    [
        html.Br(),
        dbc.CardImg(src="/assets/vBar.png", top=True),
        dbc.CardBody(
            [
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H2("Total Profit per Product Line", className="card-title"),
                dbc.Button("View Graph", color="primary", id="open-modal3", disabled=False),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Header"),
                        dbc.ModalBody(dbc.Row(dbc.Col([dcc.Graph(id="graph3"), dcc.Interval(id="update-graph3", interval=1000)]))),
                        dbc.ModalFooter(dbc.Button("Close", id="close-modal3", color="primary", size="md"))
                    ],
                    id="modal3",
                    size="lg",
                    centered=True
                )
            ]
        ),
    ]
)

@app.callback( Output("modal3", "is_open"), [Input("open-modal3", "n_clicks"), Input("close-modal3", "n_clicks")], [State("modal3", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("graph3", "figure"), [Input("update-graph3", "n_intervals")])
def update_graph3(input_data):
    x_values = list(Graph3_Data.get("Retail").keys())
    direct_marketing = list(Graph3_Data.get("Direct Marketing").values())
    ecommerce = list(Graph3_Data.get("Ecommerce").values())
    retail = list(Graph3_Data.get("Retail").values())
    #revenue = list(Graph2_Data.values())

    for i in range(len(x_values)):
        random_num_dm = random.uniform(0.9, 1.1)
        random_num_em = random.uniform(0.9, 1.1)
        random_num_rt = random.uniform(0.9, 1.1)
        #random_num_re = random.uniform(0.9, 1.1)
        direct_marketing[i] = direct_marketing[i] * random_num_dm
        ecommerce[i] = ecommerce[i] * random_num_em
        retail[i] = retail[i] * random_num_rt
        #revenue[i] = revenue[i] * random_num_re
    
    data_dm = go.Bar(
        x = x_values,
        y = direct_marketing,
        name="Direct Marketing",

    )
    data_em = go.Bar(
        x= x_values,
        y= ecommerce,
        name="Ecommerce"
    )
    data_rt = go.Bar(
        x= x_values,
        y= retail,
        name= "Retail"
    )
    '''
    data_re = go.Bar(
        x= x_values,
        y= revenue,
        name= "Revenue"
    )
    '''

    layout = {
        "title": "Sum of Profit per Product Line per Channel (USD)",
        "barmode": "group",
        "bargap": 0.5,
        "clickmode": "event+select"
    }

    return {"data": [data_dm, data_rt, data_em], "layout": layout}
################################################################################################################################################################


card6 = dbc.Card(
    [
        dbc.CardImg(src="/assets/hBar.png", top=True),
        dbc.CardBody(
            [
                html.H2("Total Product Cost per Product Line", className="card-title"),
                dbc.Button("View Graph", color="primary", id="open-modal5", disabled=False),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Header"),
                        dbc.ModalBody(dbc.Row(dbc.Col([dcc.Graph(id="graph5"), dcc.Interval("update-graph5", interval=1000)]))),
                        dbc.ModalFooter(dbc.Button("Close", size="md", color="primary", id="close-modal5"))
                    ],
                    id="modal5",
                    size="lg",
                    centered=True
                )
            ]
        ),
    ]
)

@app.callback( Output("modal5", "is_open"), [Input("open-modal5", "n_clicks"), Input("close-modal5", "n_clicks")], [State("modal5", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("graph5", "figure"), [Input("update-graph5", "n_intervals")])
def update_graph5(input_data):
    x_values = list(Graph5_Data.keys())
    y_values = list(Graph5_Data.values())

    for i in range(len(y_values)):
        random_num = random.uniform(0.9, 1.1)
        y_values[i] = y_values[i] * random_num
    
    data = go.Bar(
        name="Product Type by Cost",
        x= y_values,
        y= x_values,
        orientation="h"
    )

    layout = {
        "title": "Sum of Product Cost per Product Line (USD)",
        "clickmode": "event+select"
    }

    return {"data": [data], "layout": layout}
################################################################################################################################################################

card7 = dbc.Card(
    [
        dbc.CardImg(src="assets/sunburst.png", top=True),
        dbc.CardBody(
            [
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H2("Product Line Sentiment", className = "card-title"),
                dbc.Button("View Graph", color = "primary", size = "md", id="open-modal7", disabled=False),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Header"),
                        dbc.ModalBody(dbc.Row(dbc.Col([dcc.Graph(id="graph7"), dcc.Interval(id="update-graph7", interval=10000)]))),
                        dbc.ModalFooter(dbc.Button("Close", color = "primary", size="md", id="close-modal7")),
                    ],
                    id = "modal7",
                    size="lg",
                    centered=True
                )
            ]
        )
    ]
)

@app.callback(Output("modal7", "is_open"), [Input("open-modal7", "n_clicks"), Input("close-modal7", "n_clicks")], [State("modal7", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("graph7", "figure"), [Input("update-graph7", "n_intervals")])
def update_graph7(input_data):
    algo = dictionary_dimension_conversion(Graph8_Data)
    dictionary_1 = algo.dict_conversion()
    total = algo.dict_total()

    labels2 = ["Total"]
    parents2 = [""]
    values2 = [total]

    for key, value in dictionary_1.items():
        labels2.append(key)
        parents2.append("Total")
        values2.append(value)

        label_extension = list(Graph8_Data.get(key).keys())

        product_line = key + " "
        product_line_list = ((product_line * len(label_extension)).split(" "))
        product_line_list.pop()
        parents_extension = product_line_list

        values_extension = list(Graph8_Data.get(key).values())

        labels2.extend(label_extension)
        parents2.extend(parents_extension)
        values2.extend(values_extension)

    data = go.Sunburst(
            labels=labels2,
            parents=parents2,
            values=values2,
            branchvalues="total",
            maxdepth=2
        )
    
    layout = {
        "title": "Popular Sentiments of each Product Line",
        "margin": {"l": 20, "t":30, "b":20, "r":20},
        "clickmode": "event+select"
    }

    return {"data": [data], "layout": layout}
################################################################################################################################################################
card8 = dbc.Card(
    [
        html.Br(),
        dbc.CardImg(src="assets/WordCloud3.png", top=True),
        dbc.CardBody(
            [
                html.Br(),
                html.Br(),
                html.H2("Consumer Comments per Product Type", className="card-title"),
                dbc.Button("View Graph", id="open-modal8", color="primary", size="md", disabled=False),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Header"),
                        dbc.ModalBody(
                            [
                                dbc.Row(dbc.Col([html.Img(src=app.get_asset_url("WordCloud3.png"), width="98%")])),
                                html.Br(),
                                dbc.Row(dbc.Col([html.Img(src=app.get_asset_url("WordCloud5.png"), width="98%")])),
                            ]
                        ),
                        dbc.ModalFooter(dbc.Button("Close", color = "primary", size="md", id="close-modal8")),
                    ],
                    id = "modal8",
                    size="xl",
                    centered=True,
                    scrollable=True
                )
            ]
        )
    ]
)

@app.callback(Output("modal8", "is_open"), [Input("open-modal8", "n_clicks"), Input("close-modal8", "n_clicks")], [State("modal8", "is_open")])
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

################################################################################################################################################################
complete_button = html.Div(
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Button("Click to conclude analysis and retrieve token", id="completed-analysis-modal-button", size="lg", color="success", disabled=False),
                    dbc.Modal(
                        [
                            dbc.ModalHeader(children=[html.H3("Your token is located below.")]), 
                            dbc.ModalBody(children=
                                [ 
                                    html.H4("DO NOT close the tab until you have copied your token and inserted it into the Qualtrics Survey"),
                                    html.Br(),
                                    html.Hr(), 
                                    html.H2(id="token", className="alert-link")
                                ]
                            ),
                            dbc.ModalFooter(
                                dbc.Button("Close",id="close-completed-analysis-modal",className="ml-auto")
                            )
                        ],
                        id="completed-analysis-modal", 
                        size="lg", 
                        centered=True
                    )
                ]
            )
        ]
    )
)

start_row = dbc.Row(
    [
        dbc.Col(
            dbc.Button("Click to start your analysis", href='/dashboard', id="start-analysis-button", size="lg", color="success", disabled=False, loading_state=False),
            width=2
        )
    ], align="center", justify="center", className="h-50"
)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/':
        return page1_layout
    else:
        return page2_layout

app.layout = html.Div([dcc.Location(id="url", refresh=False), html.Div(id='page-content')])
page1_layout = html.Div([start_row], style={"height": "200vh"})


row0 = dbc.Row(children=[dbc.Col(children=cheating_button, align="center")])
row1 = dbc.Row([dbc.Col(id="card1", children=[card1], width=4), dbc.Col(id="card3", children=[card3], md=4), dbc.Col(id="card7", children=[card7], md=4)])
row2 = dbc.Row([dbc.Col(id="card4", children=[card4], md=4), dbc.Col(id="card5", children=[card5], md=4), dbc.Col(id="card8", children=[card8], md=4)]) #dbc.Col(id="card6", children=[card6], md=4)
row3 = dbc.Row([dbc.Col(id="end", children=complete_button, align="center")])

page2_layout = html.Div([row0, row1, row2, row3])


if __name__ == "__main__":
    app.run_server(debug=True)
################################################################################################################################################################