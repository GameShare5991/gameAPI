#GameShare game API
#Andrew James

from flask import Flask, jsonify
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
    gamelist = []
    for game in games:
        gamelist.append(str(game.to_dict()))
    return jsonify(gamelist) 

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
@app.route('/games/<gameid>/image', methods=['GET'])
def gameimage(gameid):
    games = db.collection('games').where("id", "==", gameid).get()
    gamelist = []
    for game in games:
        gamelist.append(str(game.to_dict()))
    dict = ast.literal_eval(gamelist[0])
    return  jsonify(dict['img'])

#delete game using it's id
@app.route('/games/delete/<gameid>', methods=['GET', 'DELETE'])
def deletegame(gameid):
    games = db.collection('games').where("id", "==", gameid).get()
    docid = games[0].id
    db.collection('games').document(docid).delete()
    return ('deleted game with gameID: '+ gameid)

#update game place holder by gameid
#@app.route('/games/update/<gameid>', methods=['GET', 'POST'])
#def updategame(gameid):
    #games = db.collection('games').where("id", "==", gameid).get()
    #docid = games[0].id
    #db.collection('games').document(docid).update()
    #return ('updated game with gameID: '+ gameid)

#create game place holder 
#@app.route('/games/create', methods=['POST'])
#def creategame():
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
