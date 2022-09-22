import random

i = 0
liste = []
while i < 45:
    i = i + 1
    liste.append(i)
d=dict()
for x in range(1,46):
    d[x]=0
temp1 = 0
temp2 = 0
def Ziehung():
    i = 0
    while i < 6:
        temp1 = random.randrange(0, 44-i)
        temp2 = liste[temp1]
        liste[temp1] = liste[44-i]
        liste[44-i] = temp2

        d[liste[44-i]] = d[liste[44-i]] + 1

        i = i + 1
zahler = 0
while zahler < 1000:
    zahler = zahler + 1
    Ziehung()
print(d)
