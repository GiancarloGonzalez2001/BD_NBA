import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import consultas as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#prueba de conexión para hacer una consulta
#Cantidad de jugadores por universidad
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.prueba(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=[ "universidad", "cantidad"])
figBarCases = px.bar(dfCases.head(20), x="universidad", y="cantidad")

#------------------------------------------


#Layout
app.layout = html.Div(children=[
    html.H1(children='Proyecto Manejo de bases de datos'),
    html.H2(children='Universidad del Rosario'),
    html.H3(children='Juan Manuel Dávila, Gianzarlo González, Ángel López'),
    dcc.Graph(
        id='prueba',
        figure=figBarCases
    ),
])

if __name__ == "__main__":
    app.run_server(debug=True)

print('vamos bien')
