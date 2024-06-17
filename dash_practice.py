import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

airline_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})


app = dash.Dash(__name__)

app.layout = html.Div(children= [html.H1('Airline Flight Dashboard',
                                         style={'textAlign':'center', 'color': '#503D36', 'font-size' : 40}),
                                 html.Div(['Input Year', dcc.Input(id = 'input-year', value='2010', type = 'number', style={'height':'50px', 'font-size':35}),],
                                          style={'font-size':40}),
                                 html.Br(),
                                 html.Br(),
                                 html.Div(dcc.Graph(id = 'bar-chart')),
                                 ])

@app.callback(Output(component_id='bar-chart', component_property='figure'),
              Input(component_id='input-year', component_property='value'))

def get_graph(entered_year):
    df=airline_data[airline_data['Year']==int(entered_year)]
    
    bar_chart = df.groupby('DestState')['Flights'].sum().reset_index()
    
    fig = px.bar(x=bar_chart['DestState'], y=bar_chart['Flights'], title='Total Number of Flights to the Destination split by reporting airline')
    fig.update_layout(xaxis_title='Destination State', yaxis_title='Number of flights', title='Flight to Desitnation State')
    return fig
    

if __name__ == '__main__':
    app.run_server()