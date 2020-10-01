import requests
import json
import re
import flask
import pandas as pd 

'''
The function will get info from rick and morty api, only characters that meet the following conditions:
    1. The character is a humen (Spicies).
    2. The character is in alive status.
    3. The fuction will check the origin of the character
'''

def getCharacters():
    url = 'https://rickandmortyapi.com/api/character?species=human&status=alive'
    earthcharacters = []
    regex = "Earth"

    #Get all characters from all pages
    while True:
        response = requests.get(url)
        data  = response.json()
        results = data["results"]
        for result in results:
            if(re.match(regex, result["origin"]["name"])):
                earthcharacters.append([result["name"], result["location"]["name"], result["image"]])

        nextPage = data["info"]["next"]
        if(nextPage is None):
            break
        url = nextPage

    chars = pd.DataFrame(earthcharacters, columns=['Name', 'Location','Image'])
    chars.to_csv('characters.csv', index=False)

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Rick And Morty API DevOPS</h1>
<p>A prototype API.</p>'''

@app.route('/healthcheck', methods=['GET'])
def checkHealth():
        url = 'https://rickandmortyapi.com/api/character'
        response = requests.get(url)
        if response:
            return '''<h1>The Api is working properly</h1>'''
        return '''<h1>The is some issue with rick and morty API</h1>'''

@app.route('/earthcharacters', methods=['GET'])
def getEChars():
    getCharacters()
    chars = pd.read_csv('characters.csv')
    return chars.to_json(orient='records')

app.run(host='0.0.0.0',port='3000')