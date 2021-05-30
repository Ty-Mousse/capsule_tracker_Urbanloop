import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
from circuit import x_circuit, y_circuit, xcm, xcM, ycm, ycM
from test import get_data
from Capsule import Capsule


# Initialisation de l'application web
external_stylesheet = ['./assets/base.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

# Initialisation de la capsule
capsule = Capsule(0)
time = 0

# Création de la figure du circuit
fig = go.Figure(data=[go.Scatter(x=x_circuit,
                                y=y_circuit,
                                mode='lines',
                                name='Circuit',
                                line=dict(width=2, color='blue'))],
                layout=go.Layout(xaxis=dict(range=[xcm, xcM], autorange=False, zeroline=False, showgrid=False, showticklabels=False),
                                yaxis=dict(range=[ycm, ycM], autorange=False, zeroline=False, showgrid=False, showticklabels=False, scaleanchor='x', scaleratio=1),
                                autosize=False,
                                width=800,
                                height=800,
                                margin=dict(l=0, r=50, b=0, t=0, pad=0),
                                showlegend=False,
                                hovermode='closest'))

# Ajout de la position initiale
fig.add_scatter(x=[0], y=[0], mode='markers', name="Capsule #1", marker=dict(size = 15), fillcolor='red')

# Ajout de l'image à la figure
fig.add_layout_image(dict(source="./assets/circuit.png",
                        xref="x",
                        yref="y",
                        x=-74500,
                        y=39500,
                        sizex=104500,
                        sizey=80000,
                        opacity=1,
                        layer="below"))

fig.update_layout(template="plotly_white")

# Corps de la page
app.layout = html.Div(className='body',
                    children=[
                            # Visualisation du circuit test
                            html.Div(className='figure', children = dcc.Graph(id='live-update-graph')),

                            # Div de placement sur la page
                            html.Div(className='content', children = [html.Div(className='header',
                                                                            children = [html.Img(id='logo',
                                                                            src=app.get_asset_url('./logo.png'),
                                                                            width='250')]),
                                                                    html.Div(className='indicateurs',
                                                                            children = [html.Div(className='indicateur-speed', children = dcc.Graph(id='live-update-speed')),
                                                                                        html.Div(className='indicateur-distance', children = dcc.Graph(id='live-update-distance'))]),]),                    

                            # Actualisation de la page toutes les 200 millisecondes
                            dcc.Interval(id='interval-component',
                                        interval=200, # in milliseconds
                                        n_intervals=0)])




# Callback permettant l'actualisation du graphe à chaque intervalle de temps
@app.callback([dash.dependencies.Output('live-update-graph', 'figure'),
              dash.dependencies.Output('live-update-speed', 'figure'),
              dash.dependencies.Output('live-update-distance', 'figure')],
              dash.dependencies.Input('interval-component', 'n_intervals'))

def update_graph_live(n):

    # Appel de la figure depuis le code principal
    global fig

    # Suppression du point présent à l'étape précédente
    new_data = list(fig.data)
    new_data.pop(1)
    fig.data = new_data

    # Mise à jour des informations de la capsule
    global time
    if time <= 781:
        (abs_curviligne, vitesse_capsule) = get_data(time)
        capsule.update_data(abs_curviligne*1000, vitesse_capsule)
    else:
        abs_curviligne = 237
        vitesse_capsule = 0
    time += 1

    # Création de la jauge de vitesse
    compteur = go.Figure(go.Indicator(mode = 'gauge+number',
                                    value = round(vitesse_capsule*3.6, 1),
                                    title = {'text': "Vitesse (km/h)"},
                                    domain = {'x': [0, 1], 'y': [0, 1]},
                                    gauge = {'axis': {'range': [None, 80]}}))

    compteur.update_layout(width=200,
                        height=300,
                        margin=dict(l=0, r=0, b=0, t=0, pad=0))

    # Création de la jauge de distance
    distance = go.Figure(go.Indicator(mode = 'gauge+number',
                                    value = abs_curviligne,
                                    title = {'text': "Distance parcourue (m)"},
                                    domain = {'x': [0, 1], 'y': [0.4, 0.6]},
                                    gauge = {'axis': {'range': [None, 300]},
                                            'shape': "bullet",}))

    distance.update_layout(width=750,
                        height=200,
                        margin=dict(l=250, r=0, b=0, t=0, pad=0))

    # Affichage de la capsule
    fig.add_scatter(x=[capsule.x], y=[capsule.y], mode='markers', name="Capsule #1", marker=dict(size = 15), fillcolor='red')

    return fig, compteur, distance




# Boucle de fonctionnement de l'application web
if __name__ == '__main__':
    app.run_server(debug=True)