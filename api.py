import requests
import json
import plotly
import plotly.express as px
import plotly.graph_objs as go


api = requests.get('https://api.covid19india.org/data.json')
api_state = api.json()['statewise']
api_cases_time_series = api.json()['cases_time_series']

dailyconfirmed = [] 
dailydeceased = []
dailyrecovered = []
date = []

for j in api_cases_time_series:
    dailyconfirmed.append(j['dailyconfirmed'])
    date.append(j['date'])
    dailydeceased.append(j['dailydeceased'])
    dailyrecovered.append(j['dailyrecovered'])


def create_plot(x, y):
    data=[go.Scatter(x=x, y=y, mode='lines+markers')]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def dailyconfirmed_graph():
    return create_plot(date, dailyconfirmed)

def dailydeceased_graph():
    return create_plot(date, dailydeceased )

def dailyrecovered_graph():
    return create_plot(date, dailyrecovered)
