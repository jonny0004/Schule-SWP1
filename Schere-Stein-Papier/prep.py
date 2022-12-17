import numpy as np
dictZähler = { "Schere": 0,
               "Papier": 0,
               "Stein": 0,
               "Echse": 0,
               "Spock": 0,
               "siegeComp": 0,
               "SiegeMen": 0,
               "Unentschieden":0,
               }
dictAlle = {"Jonny": dictZähler}
np.save('daten.npy', dictAlle)
