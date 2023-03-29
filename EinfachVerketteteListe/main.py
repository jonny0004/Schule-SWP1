import random


class ListElement():
    def __init__(self, obj):
        self.obj = obj
        self.nextElement = None

    def setNextElem(self, nextElem):
        self.nextElement = nextElem

    def getNextElem(self):
        return self.nextElement

    def getObj(self):
        return self.obj


class EinfacheListe():
    def __init__(self):
        self.startElem = ListElement("Kopf")


    def getFirstElem(self):
        return self.startElem

    def getLastElem(self):
        le = self.startElem
        while le.getNextElem() is not None:
            le = le.getNextElem()
        return le

    def addLast(self, obj):
        newElem = ListElement(obj)
        lastElem = self.getLastElem()
        lastElem.setNextElem(newElem)

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
        newElem.setNextElem(nextElem)

    def delete(self, o):
        le = self.startElem
        while le.getNextElem() is not None and not le.getObj() == o:
            if le.getNextElem().getObj() == o:
                if le.getNextElem().getNextElem() is not None:
                    le.setNextElem(le.getNextElem().getNextElem())
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
        return i-1




def main():
    liste1 = EinfacheListe()
    for i in range(0,100):
       liste1.addLast(random.randrange(1,100))

    liste1.writeList()
    print(liste1.laenge())


if __name__ == "__main__":
    main()
