import random


class ListElement():
    
    def __init__(self, obj):
        self.obj = obj
        self.nextElement = None
        self.previousElement = None

    def setNextElem(self, nextElem):
        self.nextElement = nextElem

    def setPrevElem(self, prevElem):
        self.previousElement = prevElem

    def getNextElem(self):
        return self.nextElement

    def getPrevElem(self):
        return self.previousElement

    def getObj(self):
        return self.obj


class DoppelteListe():


    def __init__(self):
        self.startElem = ListElement("Kopf")
        self.endElem = ListElement("Ende")
        self.startElem.setNextElem(self.endElem)
        self.endElem.setPrevElem(self.startElem)

    def getFirstElem(self):
        return self.startElem

    def getLastElem(self):
        return self.endElem


    def addLast(self, obj):
        newElem = ListElement(obj)
        lastElem = self.getLastElem()
        previous = lastElem.getPrevElem()
        previous.setNextElem(newElem)
        newElem.setNextElem(lastElem)
        newElem.setPrevElem(previous)
        lastElem.setPrevElem(newElem)

    def find(self, o):
        le = self.startElem

        while le is not None:

            if le.getObj() == o:
                return "True"
            le = le.getNextElem()

        return "False"

    def writeList(self):
        le = self.startElem
        while le is not None:
            print(le.getObj())
            le = le.getNextElem()

    def insertAfter(self, prevItem, newItem):
        pointerElem = self.startElem.getNextElem()
        while pointerElem is not None and not pointerElem.getObj() == prevItem:
            pointerElem = pointerElem.getNextElem()

        newElem = ListElement(newItem)
        nextElem = pointerElem.getNextElem()
        pointerElem.setNextElem(newElem)
        newElem.setPrevElem(pointerElem)
        nextElem.setPrevElem(newElem)
        newElem.setNextElem(nextElem)


    def delete(self, o):
        le = self.startElem
        while le.getNextElem() is not None and not le.getObj() == o:
            if le.getNextElem().getObj() == o:
                if le.getNextElem().getNextElem() is not None:
                    nextnext = le.getNextElem().getNextElem()
                    le.setNextElem(nextnext)
                    nextnext.setPrevElement(le)
                else:
                    le.setNextElem(None)
                    break

            le = le.getNextElem()

    def laenge(self):
        i = 0
        le = self.startElem
        while le is not None:
            i = i +1
            le = le.getNextElem()
        return i -2


def main():
    liste1 = DoppelteListe()
    for i in range(0,100):
       liste1.addLast(random.randrange(1,100))

    liste1.writeList()
    print(liste1.laenge())


if __name__ == "__main__":
    main()
