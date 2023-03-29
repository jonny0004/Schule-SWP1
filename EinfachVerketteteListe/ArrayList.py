import random


class DoppelteListe():
    def __init__(self):
        self.liste = []


    def addLast(self, obj):
        self.liste.append(obj)

    def find(self, o):
        if o in self.liste:
            return True
        else:
            return False

    def writeList(self):
        for x in range(len(self.liste)):
            print(self.liste[x])

    def insertAfter(self, prevItem, newItem):
        self.liste.insert(self.liste.index(prevItem)+1,newItem)


    def delete(self, o):
        self.liste.remove(o)

    def laenge(self):
        return len(self.liste)

def main():
    liste1 = DoppelteListe()
    for i in range(0,100):
       liste1.addLast(random.randrange(1,100))

    liste1.writeList()
    print(liste1.laenge())


if __name__ == "__main__":
    main()
