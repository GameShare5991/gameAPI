#GameShare game API
#Andrew James

from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import ast

# Use the application default credentials
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

#display all games in db
@app.route('/games', methods=['GET'])
def allgames():
    games = db.collection('games').get()
    gamelist = []
    for game in games:
        gamelist.append(str(game.to_dict()))
    return jsonify(gamelist)

#get game by ID
@app.route('/games/<gameid>', methods=['GET'])
def gamenames(gameid):
    games = db.collection('games').where("id", "==", gameid).get()
    game = str(games[0].to_dict())
    return jsonify(game)

#display all xbox games
@app.route('/games/xbox', methods=['GET'])
def xboxgames():
    games = db.collection('games').where("console", "array_contains", "xbox" ).get()
    gamelist = []
    for game in games:
        gamelist.append(str(game.to_dict()))
    return jsonify(gamelist)  

#display all n64 games
@app.route('/games/n64', methods=['GET'])
def n64games():
    games = db.collection('games').where("console", "array_contains", "n64" ).get()
    gamelist = []
    for game in games:
        gamelist.append(str(game.to_dict()))
    return jsonify(gamelist)  

#display all pc games
@app.route('/games/pc', methods=['GET'])
def pcgames():
    games = db.collection('games').where("console", "array_contains", "pc" ).get()
    gamelist = []
    for game in games:
        gamelist.append(str(game.to_dict()))
    return jsonify(gamelist)  

#display all ps5 ganes
@app.route('/games/ps5', methods=['GET'])
def ps5games():
    games = db.collection('games').where("console", "array_contains", "ps5" ).get()
    gamelist = []
    for game in games:
        gamelist.append(str(game.to_dict()))
    return jsonify(gamelist)  

#display all switch ganes
@app.route('/games/switch', methods=['GET'])
def switchgames():
    games = db.collection('games').where("console", "array_contains", "switch" ).get()
    gamelist = []
    for game in games:
        gamelist.append(str(game.to_dict()))
    return jsonify(gamelist)  

#displays image location in firebase storage for use in frontend
@app.route('/games/image/<gameid>', methods=['GET'])
def gameimage(gameid):
    games = db.collection('games').where("id", "==", gameid).get()
    game = str(games[0].to_dict())
    dict = ast.literal_eval(game)
    return  jsonify(dict['img'])

#delete game using it's id
@app.route('/games/delete/<gameid>', methods=['GET', 'DELETE'])
def deletegame(gameid):
    games = db.collection('games').where("id", "==", gameid).get()
    docid = games[0].id
    db.collection('games').document(docid).delete()
    return ('deleted game with gameID: '+ gameid)

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
    return 'added to database'

#update game by id
@app.route('/games/update/<gameid>', methods=['POST'])
def update(gameid):
    request_data = request.get_json()
    games = db.collection('games').where("id", "==", gameid).get()
    docid = games[0].id
    title = "None"
    rating = "None"
    descrip = "None"
    released = "None"
    id = "None"
    console = []

    if 'console' in request_data:
        for item in request_data['console']:
            console.append(item)
        db.collection('games').document(docid).update({'console' : console})

    if 'title' in request_data:
        title = request_data['title']
        db.collection('games').document(docid).update({'title' : title})

    if 'rating' in request_data:
        rating = request_data['rating']
        db.collection('games').document(docid).update({'rating' : rating})

    if 'descrip' in request_data:
        descrip = request_data['descrip']
        db.collection('games').document(docid).update({'descrip' : descrip})

    if 'released' in request_data:
        released = request_data['released']
        db.collection('games').document(docid).update({'released' : released})

    if 'id' in request_data:
        id = request_data['id']
        db.collection('games').document(docid).update({'id' : id})

    return ('updated game with gameID')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
