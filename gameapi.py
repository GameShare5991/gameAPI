#GameShare game API
#Andrew James

from flask import Flask, request
import firebase_admin
from firebase_admin import credentials, firestore
import json
from flask_cors import CORS

# Use the application default credentials
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)
CORS(app)

#display all games in db
@app.route('/games', methods=['GET'])
def allgames():
    games = db.collection('games').get()
    gamelist = []
    for game in games:
        gamelist.append(game.to_dict())
    return json.dumps(gamelist)

#get game by ID
@app.route('/games/<gameid>', methods=['GET'])
def gamenames(gameid):
    games = db.collection('games').where("id", "==", gameid).get()
    game = games[0].to_dict()
    return json.dumps(game)

#display all xbox games
@app.route('/games/xbox', methods=['GET'])
def xboxgames():
    games = db.collection('games').where("console", "array_contains", "xbox" ).get()
    gamelist = []
    for game in games:
        gamelist.append(game.to_dict())
    return json.dumps(gamelist)  

#display all n64 games
@app.route('/games/n64', methods=['GET'])
def n64games():
    games = db.collection('games').where("console", "array_contains", "n64" ).get()
    gamelist = []
    for game in games:
        gamelist.append(game.to_dict())
    return json.dumps(gamelist)  

#display all pc games
@app.route('/games/pc', methods=['GET'])
def pcgames():
    games = db.collection('games').where("console", "array_contains", "pc" ).get()
    gamelist = []
    for game in games:
        gamelist.append(game.to_dict())
    return json.dumps(gamelist)  

#display all ps5 ganes
@app.route('/games/ps5', methods=['GET'])
def ps5games():
    games = db.collection('games').where("console", "array_contains", "ps5" ).get()
    gamelist = []
    for game in games:
        gamelist.append(game.to_dict())
    return json.dumps(gamelist)  

#display all switch ganes
@app.route('/games/switch', methods=['GET'])
def switchgames():
    games = db.collection('games').where("console", "array_contains", "switch" ).get()
    gamelist = []
    for game in games:
        gamelist.append(game.to_dict())
    return json.dumps(gamelist)  

#displays image
@app.route('/games/image/<gameid>', methods=['GET'])
def gameimage(gameid):
    games = db.collection('games').where("id", "==", gameid).get()
    game = games[0].to_dict()
    imgid = game['img']
    return f"<img src = \"{imgid}\">"
 

#delete game using it's id
@app.route('/games/delete/<gameid>', methods=['GET', 'DELETE'])
def deletegame(gameid):
    games = db.collection('games').where("id", "==", gameid).get()
    docid = games[0].id
    db.collection('games').document(docid).delete()
    return '',204

#create new game
@app.route('/games/create', methods=['POST'])
def updategame():
    request_data = request.get_json()
    title = "None"
    rating = "None"
    descrip = "None"
    released = "None"
    id = "None"
    console = []
    data = {}
    
    if 'console' in request_data:
        for item in request_data['console']:
            console.append(item)

    if 'title' in request_data:
        title = request_data['title']

    if 'rating' in request_data:
        rating = request_data['rating']

    if 'descrip' in request_data:
        descrip = request_data['descrip']

    if 'released' in request_data:
        released = request_data['released']

    if 'id' in request_data:
        id = request_data['id']

    data = {'title' : title, 'rating' : rating, 'descrip' : descrip, 'id' : id, 'released' : released, 'console' : console}
    db.collection('games').add(data)
    
    return '',201

#update game by id
@app.route('/games/update/<gameid>', methods=['PATCH'])
def update(gameid):
    request_data = request.get_json()
    games = db.collection('games').where("id", "==", gameid).get()
    docid = games[0].id
    title = "None"
    rating = "None"
    descrip = "None"
    released = "None"
    console = []
    data = {}

    if 'console' in request_data:
        for item in request_data['console']:
            console.append(item)
        data['console'] = console

    if 'title' in request_data:
        title = request_data['title']
        data['title'] = title

    if 'rating' in request_data:
        rating = request_data['rating']
        data['rating'] = rating

    if 'descrip' in request_data:
        descrip = request_data['descrip']
        data['descrip'] = descrip

    if 'released' in request_data:
        released = request_data['released']
        data['released'] = released

    data = {"title" : title, "rating" : rating, "descrip" : descrip, "released" : released, "console" : console}
    db.collection('games').document(docid).update(data)
    
    return '',200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
