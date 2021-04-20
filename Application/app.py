import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
from circuit import x_circuit, y_circuit, xcm, xcM, ycm, ycM
from test import get_data
from Capsule import Capsule


# Initialisation de l'application web
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Initialisation de la capsule
capsule = Capsule(0)
time = 0




# Corps de la page
app.layout = html.Div(children=[
                            # Header
                            html.Div(id='header',
                                    children = [html.Img(id='logo',
                                                        src=app.get_asset_url('./logo.png'),
                                                        width='250'),
                                                html.H1(children='Visualisation du circuit test',
                                                        style={'text-align': 'center',
                                                                'margin-top': '15px',
                                                                'font-family': 'Arial',
                                                                'font-size': '30px'})],
                                    style = {'display': 'flex',
                                            'flex-direction': 'column',
                                            'align-items': 'center'}),
                            
                            # Visualisation de la vitesse de la capsule
                            html.Div(children = dcc.Graph(id='live-update-speed')),

                            # Visualisation de la distance parcourue
                            html.Div(children = dcc.Graph(id='live-update-distance')),

                            # Visualisation du circuit test
                            html.Div(children = dcc.Graph(id='live-update-graph'),
                                    style={'display': 'flex',
                                        'flex-direction': 'column',
                                        'align-items': 'center'}),

                            # Actualisation de la page toutes les 200 millisecondes
                            dcc.Interval(id='interval-component',
                                        interval=200, # in milliseconds
                                        n_intervals=0)
])




# Callback permettant l'actualisation du graphe à chaque intervalle de temps
@app.callback([dash.dependencies.Output('live-update-graph', 'figure'),
              dash.dependencies.Output('live-update-speed', 'figure'),
              dash.dependencies.Output('live-update-distance', 'figure')],
              dash.dependencies.Input('interval-component', 'n_intervals'))

def update_graph_live(n):
    # Création de la figure du circuit
    fig = go.Figure(data=[go.Scatter(x=x_circuit,
                                    y=y_circuit,
                                    mode='lines',
                                    name='Circuit',
                                    line=dict(width=2, color='blue'))],
                    layout=go.Layout(xaxis=dict(range=[xcm, xcM], autorange=False, zeroline=False),
                                    yaxis=dict(range=[ycm, ycM], autorange=False, zeroline=False, scaleanchor='x', scaleratio=1),
                                    autosize=False,
                                    width=850,
                                    height=850,
                                    showlegend=False,
                                    title_text="Position de la capsule",
                                    hovermode='closest'))

    # Mise à jour des informations de la capsule
    global time
    if time <= 781:
        (abs_curviligne, vitesse_capsule) = get_data(time)
        capsule.update_data(abs_curviligne*1000, vitesse_capsule)
    else:
        vitesse_capsule = 0
    time += 1

    # Création de la jauge de vitesse
    compteur = go.Figure(go.Indicator(mode = 'gauge+number',
                                    value = round(vitesse_capsule*3.6, 1),
                                    title = {'text': "Vitesse (km/h)"},
                                    domain = {'x': [0, 1], 'y': [0, 1]},
                                    gauge = {'axis': {'range': [None, 100]}}))

    # Création de la jauge de distance
    distance = go.Figure(go.Indicator(mode = 'gauge+number',
                                    value = abs_curviligne,
                                    title = {'text': "Distance parcourue (m)"},
                                    domain = {'x': [0, 1], 'y': [0.4, 0.6]},
                                    gauge = {'axis': {'range': [None, 500]},
                                            'shape': "bullet",}))

    # Affichage de la capsule
    fig.add_scatter(x=[capsule.x], y=[capsule.y], mode='markers', name="Capsule #1", marker=dict(size = 15), fillcolor='red')

    return fig, compteur, distance




# Boucle de fonctionnement de l'application web
if __name__ == '__main__':
    app.run_server(debug=True)