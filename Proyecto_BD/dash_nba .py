import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import consultas as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
bg_color = '#A7E6EE'
div_color = '#D1F1F5'
font_color_bar = '#000000'
label_bg = '#4C92FE'
label_color = '#FFFFFF'
rosario_color = '#F00A0A'
ur = 20
title = 60
subtitle = 40
label = 30
#prueba de conexión para hacer una consulta
#Cantidad de jugadores por universidad
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.prueba(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=[ "universidad", "cantidad"])
figBarCases = px.bar(dfCases.head(80), x="universidad", y="cantidad")
figBarCases.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)

con.openConnection()
query = pd.read_sql_query(sql.edad_partidos(), con.connection)
con.closeConnection()
dfAge = pd.DataFrame(query, columns=[ "edad", "cantidad"])
figAge = px.bar(dfAge.head(40), x="edad", y="cantidad")
figAge.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)

con.openConnection()
query = pd.read_sql_query(sql.puntos_por_jugador(), con.connection)
con.closeConnection()
dfPts = pd.DataFrame(query, columns=[ "nombre", "puntos"])
figPts = px.bar(dfPts.head(40), x="nombre", y="puntos")
figPts.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)

#top 20 mejor promedio de rebotes por jugador
con.openConnection()
query = pd.read_sql_query(sql.rebotes_por_jugador(), con.connection)
con.closeConnection()
dfRebs = pd.DataFrame(query, columns=[ "nombre", "rebotes"])
figRebs = px.bar(dfRebs.head(20), x="nombre", y="rebotes")
figRebs.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)
#top 20 mejor promedio de asistencias por jugador
con.openConnection()
query = pd.read_sql_query(sql.asistencias_por_jugador(), con.connection)
con.closeConnection()
dfAsis = pd.DataFrame(query, columns=[ "nombre", "asistencias"])
figAsis = px.bar(dfAsis.head(20), x="nombre", y="asistencias")
figAsis.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)
#top 20 mejor promedio net rating por jugador
con.openConnection()
query = pd.read_sql_query(sql.net_rating_por_jugador(), con.connection)
con.closeConnection()
dfNetR = pd.DataFrame(query, columns=[ "nombre", "net_rating"])
figNetR = px.bar(dfNetR.head(20), x="nombre", y="net_rating")
figNetR.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)

# 1996
con.openConnection()
query = pd.read_sql_query(sql.nacionalidad_1996(), con.connection)
con.closeConnection()
num_p_96= pd.DataFrame(query, columns=[ "pais", "total"])
fi_96= px.pie(num_p_96, values="total", names= "pais",title= "")
figMap_96 = px.choropleth(num_p_96, locations="pais",
                            locationmode="country names",
                            color="total",
                            hover_name="pais",
                            color_continuous_scale=px.colors.sequential.Purples,
                            )
figMap_96.update_layout(geo=dict(bgcolor= bg_color))

# 2008
con.openConnection()
query = pd.read_sql_query(sql.nacionalidad_2008(), con.connection)
con.closeConnection()
num_p_08= pd.DataFrame(query, columns=[ "pais", "total"])
fi_08= px.pie(num_p_08, values="total", names= "pais",title= "")
figMap_08=px.choropleth(num_p_08, locations="pais",
                            locationmode="country names",
                            color="total",
                            hover_name="pais",
                            color_continuous_scale=px.colors.sequential.Reds)
figMap_08.update_layout(geo=dict(bgcolor= bg_color))

# 2019
con.openConnection()
query = pd.read_sql_query(sql.nacionalidad_2019(), con.connection)
con.closeConnection()
num_p_19= pd.DataFrame(query, columns=[ "pais", "total"])
fi_19= px.pie(num_p_19, values="total", names= "pais",title= "")
figMap_19=px.choropleth(num_p_19, locations="pais",
                            locationmode="country names",
                            color="total",
                            hover_name="pais",
                            color_continuous_scale=px.colors.sequential.Plasma)
figMap_19.update_layout(geo=dict(bgcolor= bg_color))

# top 20 mejor promedio de rebs defensivos
con.openConnection()
query = pd.read_sql_query(sql.reb_def_por_jugador(), con.connection)
con.closeConnection()
dfdreb = pd.DataFrame(query, columns=[ "nombre", "reb_defensivo"])
figdreb = px.bar(dfdreb.head(20), x="nombre", y="reb_defensivo")
figdreb.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)
# top 20 mejor promedio de rebs ofensivos
con.openConnection()
query = pd.read_sql_query(sql.reb_ofensivo_por_jugador(), con.connection)
con.closeConnection()
dforeb = pd.DataFrame(query, columns=[ "nombre", "reb_ofensivo"])
figoreb = px.bar(dforeb.head(20), x="nombre", y="reb_ofensivo")
figoreb.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)

#top 20 jugadores por uso
con.openConnection()
query = pd.read_sql_query(sql.uso(), con.connection)
con.closeConnection()
dfuso = pd.DataFrame(query, columns=[ "nombre", "participacion"])
figuso = px.bar(dfuso.head(20), x="nombre", y="participacion")
figuso.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)
#top 20 jugadores por tiro real
con.openConnection()
query = pd.read_sql_query(sql.tiro_real(), con.connection)
con.closeConnection()
dftreal = pd.DataFrame(query, columns=[ "nombre", "tiro_real"])
figtreal = px.bar(dftreal.head(20), x="nombre", y="tiro_real")
figtreal.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)
#rebotes por altura
con.openConnection()
query = pd.read_sql_query(sql.estatura_rebotes(), con.connection)
con.closeConnection()
dftrebalt = pd.DataFrame(query, columns=[ "rebotes", "estatura"])
figrebalt = px.bar(dftrebalt.head(20), x="rebotes", y="estatura")
figrebalt.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)
#universidades con juagores con mejor promedio de net_rating
con.openConnection()
query = pd.read_sql_query(sql.univ_net_rating(), con.connection)
con.closeConnection()
dfunet = pd.DataFrame(query, columns=[ "universidad", "cantidad"])
figunet = px.bar(dfunet.head(20), x="universidad", y="cantidad")
figunet.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)
#universidades con juagores con mejor promedio de pj
con.openConnection()
query = pd.read_sql_query(sql.univ_pj(), con.connection)
con.closeConnection()
dfpj = pd.DataFrame(query, columns=[ "universidad", "p_jugados"])
figpj = px.bar(dfpj.head(20), x="universidad", y="p_jugados")
figpj.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)

#universidades con juagores con mejor promedio de puntos
con.openConnection()
query = pd.read_sql_query(sql.univ_puntos(), con.connection)
con.closeConnection()
dfupts = pd.DataFrame(query, columns=[ "universidad", "puntos"])
figupts = px.bar(dfupts.head(20), x="universidad", y="puntos")
figupts.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)
#universidades con juagores con mejor promedio de asistencias
con.openConnection()
query = pd.read_sql_query(sql.univ_asis(), con.connection)
con.closeConnection()
dfuasis = pd.DataFrame(query, columns=[ "universidad", "asistencias"])
figuasis = px.bar(dfuasis.head(20), x="universidad", y="asistencias")
figuasis.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)
#universidades con juagores con mejor promedio de rebotes
con.openConnection()
query = pd.read_sql_query(sql.univ_rebs(), con.connection)
con.closeConnection()
dfurebs = pd.DataFrame(query, columns=[ "universidad", "rebotes"])
figurebs = px.bar(dfurebs.head(20), x="universidad", y="rebotes")
figurebs.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)
#universidades con juagores con mejor promedio de uso
con.openConnection()
query = pd.read_sql_query(sql.univ_uso(), con.connection)
con.closeConnection()
dfuuso = pd.DataFrame(query, columns=[ "universidad", "participacion"])
figuuso = px.bar(dfuuso.head(20), x="universidad", y="participacion")
figuuso.update_layout(
    plot_bgcolor=bg_color,
    paper_bgcolor=div_color,
    font_color=font_color_bar
)

####
#prueba de una tabla
# fig = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
#                  cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
#                      ])

#------------------------------------------


#Layout
app.layout = html.Div(style={'background':div_color}, children=[
    html.H1(children='Universidad del Rosario', style={'backgroundColor':bg_color, 'color':rosario_color, 'font-size':ur}),
    html.H1(children='Análisis de Datos de la NBA', className = 'text-center', style={'background':bg_color}),
    html.H1(children='1996 a 2019', className = 'text-center', style={'background':bg_color, 'font-size':ur}),
    html.Div(className="row mt-4", children=[
        #Col for bars
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Jugadores por Universidad"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='prueba',
                        figure=figBarCases
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
        #Col for map
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Edad de jugadores por partidos jugados"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='edad_partidos',
                        figure=figAge
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
    ]),
    html.Div(className="row mt-4", children=[
        #Col for bars
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Mejores promedios de puntaje por jugador"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='puntos_por_jugador',
                        figure=figPts
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
        #Col for map
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Mejores promedios de rebote por jugador"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='rebotes_por_jugador',
                        figure=figRebs
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
    ]),
    html.Div(className="row mt-4", children=[
        #Col for bars
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Mayores asistencias por jugador"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='asistencias_por_jugador',
                        figure=figAsis
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
        #Col for map
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Mejores calificaciones de red (Net-Rating)"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='net_rating',
                        figure=figNetR
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
    ]),


# 1996 dash
   html.Div(className="row mt-4", children=[
        #Col for bars
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Nacionalidades 1996"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id="nacionalidadBar_1996",
                        figure=fi_96
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
        #Col for map
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Nacionalidades 1996"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id="nacionalidadMap_1996",
                        figure=figMap_96
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
    ]),
    # 2008 dash
    html.Div(className="row mt-4", children=[
        #Col for bars
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Nacionalidades 2008"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id="nacionalidadBar_2008",
                        figure=fi_08
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
        #Col for map
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Nacionalidades 2008"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id="nacionalidadMap_2008",
                        figure=figMap_08
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
    ]),
    # 2019 dash
    html.Div(className="row mt-4", children=[
        #Col for bars
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Nacionalidades 2019"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id="nacionalidadBar_2019",
                        figure=fi_19
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
        #Col for map
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Nacionalidades 2019"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id="nacionalidadMap_2019",
                        figure=figMap_19
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
    ]),
    html.Div(className="row mt-4", children=[
        #Col for bars
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Histórico de rebotes defensivos"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='reb_histo_dreb',
                        figure=figdreb
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
        #Col for map
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Histórico de rebotes ofensivos"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='reb_histo_oreb',
                        figure=figoreb
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
    ]),


    html.Div(className="row mt-4", children=[
        #Col for bars
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Histórico de participación"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='uso_hist',
                        figure=figuso
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
        #Col for map
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Mejores promedios de tiro real"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='treal_hist',
                        figure=figtreal
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
    ]),


    html.Div(className="row mt-4", children=[
        #Col for bars
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Número de rebotes por rango de estatura"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='rebs-altura',
                        figure=figrebalt
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
        #Col for map
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Mejores promedio de calificación de red (Net-Rating)"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='univ_net_rating',
                        figure=figunet
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
    ]),


    html.Div(className="row mt-4", children=[
        #Col for bars
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Partidos jugados por universidad"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='univ_pj',
                        figure=figpj
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
        #Col for map
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Puntos anotados por universidad"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='univ_pts',
                        figure=figupts
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
    ]),


    html.Div(className="row mt-4", children=[
        #Col for bars
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Mayores asistencias por universidad"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='univ_asis',
                        figure=figuasis
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
        #Col for map
        html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Mejores promedios de rebotes totales"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='univ_rebs',
                        figure=figurebs
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),
    ]),
    html.Div(className="col-12 col-xl-6", children=[
            html.Div(className="card", children=[
                html.Div(className="card-header", children=[
                    html.H3(children="Mejores promedios de participación totales"),
                ], style={'background':label_bg, 'color':label_color}),
                html.Div(className="card-body", children=[
                    dcc.Graph(
                        id='univ_uso',
                        figure=figuuso
                    ),
                ], style={'background':div_color, 'color':div_color}),
            ]),
        ]),


    html.H1(children='Juan Manuel Dávila, Gianzarlo González, Ángel López', style={'background':bg_color,'color':font_color_bar, 'font-size':ur}),

])
if __name__ == "__main__":
    app.run_server(debug=True)

print('vamos bien')
