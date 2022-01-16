import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import twitter
import tweepy
import json
import re
import requests
from textblob import TextBlob

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    dcc.Input(id='my-id',

     type='text', 
     placeholder='Enter Name to analyse in the format name*', 
     style = {

     'size': '180'
     }

     ),
    html.Div(id='output'),

    
])


@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
    )
def update_output_div(input_value):
	if input_value is None or input_value == '':
		return "You have no input, please enter an input"
	else:
		
		api_key = 'MII1k9ufkNqLZmDc933sjWF6d'

		api_secret_key = 'plfwEQu7qaHjO6EaiBC61sOd30bK1d7plmPVEzimcBKewiGHJA'

		access_token ='1204573020091830277-Dnt8v80wThS3S9tit7Skg7SvwazFUN' 

		access_token_secret = '7TE9yKHFpkTw7ppQK8xIW34r1sIwJjKfWlRzN8GnwOvlC' 

		r = requests.post('https://api.twitter.com/oauth2/token',
		                  auth=(api_key, api_secret_key),
		                  headers={'Content-Type':
		                      'application/x-www-form-urlencoded;charset=UTF-8'},
		                  data='grant_type=client_credentials')
		assert r.json()['token_type'] == 'bearer'
		bearer = r.json()['access_token']

		url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23'+input_value+'&result_type=mixed&count=100&include_entities=false'
		r = requests.get(url, headers={'Authorization': 'Bearer ' + bearer})
		r = r.json()
		print(len(r['statuses']))
		tweets = []
		for num in range(len(r['statuses'])):
		    tweets.append(r['statuses'][num]['text'])
		
		#subjectivity ranges from 0 to 1 where 0 is very objective and 1 is very subjective 
		#polarity
		#greater than 0 is positive
		# less than 0 is negative 
		#and 0 is neutral 
		positive_count = 1
		negative_count = 1
		neutral_count = 1
		total = positive_count + negative_count + neutral_count
		texts = 0
		# tweets = twitterdata.get_twitter_data()
		for t in tweets:
			texts +=1 
			analysis = TextBlob(t)
			if analysis.sentiment.polarity > 0.1:

				if analysis.sentiment.polarity > 0 and analysis.sentiment.subjectivity < 0.7:
					positive_count += 1
			elif analysis.sentiment.polarity < 0.1:
				if analysis.sentiment.polarity < 0 and analysis.sentiment.subjectivity < 0.7:
					negative_count += 1 
			else:
				neutral_count += 1
		
		positive_count = (positive_count/total)*100
		negative_count = (negative_count/total)*100
		neutral_count = (neutral_count/total)*100
		total = positive_count + negative_count + neutral_count
		print(positive_count, negative_count, neutral_count)
		return 'You\'ve entered "{}"'.format(input_value), dcc.Graph(
			id ='graph',
        figure = {
        'data' : [
         {'x': ['Positive', 'Negative', 'Neutral'], 'y':[positive_count, negative_count, neutral_count], 'type':'bar', 'name': 'twitter'}


        ],
        'layout': {
        'title': 'CURRENT TWITTER SENTIMENTS FOR {}'.format(input_value.upper())
        }

        }
        










			)
		





if __name__ == '__main__':
    app.run_server(debug=True)