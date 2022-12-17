import ast
import json
import random
import this

import numpy as np
import requests as requests

hand = ["Schere", "Papier","Stein","Echse","Spock"]
siegeComputer = 0
siegeMensch = 0
unentschieden = 0
user = ""

dictZähler = { "Schere": 0,
               "Papier": 0,
               "Stein": 0,
               "Echse": 0,
               "Spock": 0,
               "siegeComp": 0,
               "SiegeMen": 0,
               "Unentschieden":0,
               }

def UserEingabe():
    print("Userame:")
    return input()

host = 'http://localhost:5000/score'


def computerAuswahl():
    print(user)
    dictAlle = requests.get('%s/%s' % (host, user)).json()
    dictAlle = ast.literal_eval(dictAlle)
    print(dictAlle["Schere"])
    print(dictAlle[list(dictAlle)[0]])
    zahler = ZählenGesamt(dictAlle)
    randomList = random.choices(hand, weights=(dictAlle[list(dictAlle)[1]]/zahler +1, dictAlle[list(dictAlle)[2]]/zahler +1 , dictAlle[list(dictAlle)[3]]/zahler+1 , dictAlle[list(dictAlle)[4]]/zahler+1, dictAlle[list(dictAlle)[0]]/zahler+1), k=5)
    return randomList[0]

def ZählenGesamt(dic):
    zahler = 0
    for d in dic:
        if(hand.count(d) > 0):

            zahler = zahler + dic[d]
    return zahler +1



def eingabePrüfung():
    print("Mögliche Auswahl Möglichkeiten:")
    print(hand)
    print("Ihre eingabe:")
    auswahl = input()

    while auswahl not in hand:
        print("Fehler bitte erneut eingeben:")
        auswahl = input()
    dictZähler[auswahl] = dictZähler[auswahl]+1
    return auswahl


def datenSpeichern():
    dictAlle = requests.get('%s/%s' % (host, user)).json()
    dictAlle = ast.literal_eval(dictAlle)
    dictTemp = {}



    for key in dictZähler:
        dictTemp[key] = dictZähler[key]

    for key in dictTemp:
        dictTemp[key] = int(dictTemp[key]) + int(dictAlle[key])

    response = requests.put('%s/%s/%s' % (host, str(dictTemp),user))
    print(response)

def resetDict():
    for key in dictZähler:
        dictZähler[key] = 0


def alleDatenAusgeben():
    dictAlle = requests.get('%s/%s' % (host,user)).json()
    dictAlle = ast.literal_eval(dictAlle)
    dictTemp = {}

    for key in dictZähler:
        dictTemp[key] = dictZähler[key]

    for key in dictTemp:
        dictTemp[key] = dictTemp[key] + int(dictAlle[key])
    print(dictTemp)


def menue():
    weiter = True
    while weiter:
        print("Was wollen sie machen:(s fuer StatistikBisher,sk fuer Statistik mit gespeicherten daten, w fuer weiterspielen, sp für speichern der Daten, b fuer beenden)")
        eingabe = input()
        if eingabe == "w":
            return True
        elif eingabe == "b":
            return False
        elif eingabe == "s":
            print(dictZähler)
        elif eingabe == "sp":
            datenSpeichern()
            resetDict()
        elif eingabe == "sk":
            alleDatenAusgeben()
        else:
            print("falsche eingabe, bitte erneut eingeben")


def spiel():
    weiter = True
    global user
    user = UserEingabe()
    while weiter:
        eingabeSpieler = eingabePrüfung()
        eingabeComputer = computerAuswahl()

        print("eingabe des Computers:" + eingabeComputer)

        if eingabeComputer == eingabeSpieler:
            print("Es ist unentschieden")
            dictZähler["Unentschieden"] = str(int(dictZähler["Unentschieden"]) +1)
        elif hand[hand.index(eingabeSpieler)-1] == eingabeComputer or hand[(hand.index(eingabeSpieler)+2)%5] == eingabeComputer:
            print("Sie haben verloren")
            dictZähler["siegeComp"] = str(int(dictZähler["siegeComp"]) +1)
        else:
            print("Sie haben gewonnen")
            dictZähler["SiegeMen"] = str(int(dictZähler["SiegeMen"]) +1)
        weiter = menue()



def main():
    spiel()

if __name__ == '__main__':
    main()
