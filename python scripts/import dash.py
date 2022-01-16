import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
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
    return 'your tweets are: "{}"'.format(tweets)

















if __name__ == '__main__':
    app.run_server(debug=True)