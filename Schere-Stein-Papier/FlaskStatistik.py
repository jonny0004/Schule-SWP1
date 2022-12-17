import ast

import numpy as np
from flask import Flask, request, render_template
from flask_restful import Resource, Api

dictSt = { "Schere": 0,
               "Papier": 0,
               "Stein": 0,
               "Echse": 0,
               "Spock": 0,
               "siegeComp": 0,
               "SiegeMen": 0,
               "Unentschieden":0,
               }

app = Flask(__name__)
api = Api(app) #Die Flask API

#Jede resource muss von der Klasse Resource erben. Alle HTTP-Methoden werden hier auf Python-Methoden abgebildet

@app.route('/')
def home():

    dicte = alleDatenAller()
    return render_template('statistiks.html', dict=dicte)


def datenSpeichern(dictZähler, name):
    dictAlle = np.load('daten.npy', allow_pickle='TRUE')
    dictAlle= dictAlle.item()
    dictAlle[name] = dictZähler
    np.save('daten.npy', dictAlle)

def alleDatenAller():
    dictAlle = np.load('daten.npy', allow_pickle='TRUE')
    dictAlle= dictAlle.item()
    return dictAlle

def alleDatenAusgeben(name):
    dictAlle = np.load('daten.npy', allow_pickle='TRUE')
    dictAlle= dictAlle.item()
    try:
        print(dictAlle[name])
        return dictAlle[name]
    except:
        return dictSt



#Speichert den Score zu bestimmten Namen
name_score = {}

class SimpleSend(Resource):
    def get(self, name):
        return str(alleDatenAusgeben(name))

class SimpleSave(Resource):
    def put(self, wert, name):
        d = ast.literal_eval(wert)
        print(d)
        datenSpeichern(d, name)
        return {"Message" : "Neu hinzugefügt"}

#Hier passiert das Mapping auf die Klasse
api.add_resource(SimpleSend, '/score/<string:name>')
api.add_resource(SimpleSave, '/score/<string:wert>/<string:name>')

if __name__ == '__main__':
    app.run(debug=True) #debug=True lädt nach den Änderungen neu
