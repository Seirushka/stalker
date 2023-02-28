from random import randrange



res = 900
res1 = 1200
size = 30
rad = 240
fps = 10
length = 1
maxx, maxy = 0, 0
c = True
v = True
m=False

cols, rows = 40, 30
TILE = 30

x, y = randrange(0, res1, size), randrange(0, res, size)

into = []

anom=[]

lock=[]
locki=[]
locki1=[]
locki11 = []
locki2 = []

# аномалии
for i in range(randrange(1, 20)):
    into.append(randrange(2, 20))
    anom.append([randrange(0, res1, size), randrange(0, res, size)])
print(into,' into')
print(anom, ' anom')

# локаторы
for o in range(randrange(3,6)):
    lock.append(([randrange(0, res1, size), randrange(0, res, size)]))
print(o, ' lock')

#интенсивность

