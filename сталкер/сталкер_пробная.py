import pygame
from random import randrange
from changes import *

pygame.init()



im = pygame.image.load('map.png')  # слово сталкер не нужно если открываешь фаил в пустой рабочей среде

x, y = randrange(0, res1, size), randrange(0, res, size)

# аномалии
anom1 = randrange(0, res1, size), randrange(0, res, size)
anom2 = randrange(0, res1, size), randrange(0, res, size)
anom3 = randrange(0, res1, size), randrange(0, res, size)
anom4 = randrange(0, res1, size), randrange(0, res, size)
anom5 = randrange(0, res1, size), randrange(0, res, size)

while [x, y] == anom1 or [x, y] == anom2 or [x, y] == anom3 or [x, y] == anom4 or [x, y] == anom5:
    x, y = randrange(0, res1, size), randrange(0, res, size)

# локаторы

lock1 = randrange(0, res1, size), randrange(0, res, size)
l1 = pygame.image.load('n.png')
lock2 = randrange(0, res1, size), randrange(0, res, size)
lock3 = randrange(0, res1, size), randrange(0, res, size)

# поле определения

loud1 = pygame.Surface((450, 450))

loud1.fill((255, 255, 255))
loud1.set_alpha(100)

# Поле зрения
#aur1 = lock1[0] + 15, lock1[1] + 15
#aur2 = lock2[0] + 15, lock2[1] + 15
#aur3 = lock3[0] + 15, lock3[1] + 15

f = lock1
print(*f)



# шрифт и вывод данных от локаторов
font = pygame.font.SysFont('Arial', 20)
t1 = font.render(str(lock1), True, pygame.Color('darkorange'))
title1 = font.render(('лок 1'), True, pygame.Color('darkorange'))
t2 = font.render(str(lock2), True, pygame.Color('darkorange'))
title2 = font.render(('лок 2'), True, pygame.Color('darkorange'))
t3 = font.render(str(lock3), True, pygame.Color('darkorange'))
title3 = font.render(('лок 1'), True, pygame.Color('darkorange'))



length = 1
man = [(x, y)]
dx, dy = 0, 0
fps = 10



surf = pygame.display.set_mode((res1 * 1.5, res))
surf.fill(pygame.Color('black'))

sc = pygame.Surface([res1, res])
clock = pygame.time.Clock()

print(anom1[0])
print(lock1[0]- size*10, lock1[0] + size*10)

while True:
    surf.blit(sc, (0, 0))
    sc.blit(im, (0, 0))
    #sc.blit(man, (x, y))

    #pygame.draw.rect(sc, pygame.Color('white'), (*anom1, size, size))

    #pygame.draw.circle(sc, pygame.Color('blue'), aur1, rad)
    #pygame.draw.circle(sc, pygame.Color('blue'), aur2, rad)
    #pygame.draw.circle(sc, pygame.Color('blue'), aur3, rad)
    sc.blit(l1, lock1)
    pygame.draw.rect(sc, pygame.Color('orange'), (*lock2, size, size))
    pygame.draw.rect(sc, pygame.Color('orange'), (*lock3, size, size))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, size, size))) for i, j in man]


    man.append((x, y))
    man = man[-length:]



    if man[-1] == anom1 or man[-1] == anom2 or man[-1] == anom3 or man[-1] == anom4 or man[-1] == anom5:
        print(x, y)
        break

    if x <= 0 or x >= res1 or y <= 0 or y >= res:
        break

    # if anom1 in s:
    #в этих условиях прописывается что если наша аномалия попадает в зону сканирования какогото из лакаторов то онк подсвечивается красным

    if (anom1[0] > lock1[0] - size*10) and (anom1[0] < lock1[0] + size*10) and (anom1[1] > lock1[1] - size*10) and (anom1[1] < lock1[1] + size*10) or (
        anom1[0] > lock2[0] - size*10) and (anom1[0] < lock2[0] + size*10) and (anom1[1] > lock2[1] - size*10) and (anom1[1] < lock2[1] + size*10) or (
        anom1[0] > lock3[0] - size*10) and (anom1[0] < lock3[0] + size*10) and (anom1[1] > lock3[1] - size*10) and (anom1[1] < lock3[1] + size*10):
        pygame.draw.rect(sc, pygame.Color('red'), (*anom1, size, size))

    if (anom2[0] > lock1[0] - size*10) and (anom2[0] < lock1[0] + size*10) and (anom2[1] > lock1[1] - size*10) and (anom2[1] < lock1[1] + size*10) or (
        anom2[0] > lock2[0] - size*10) and (anom2[0] < lock2[0] + size*10) and (anom2[1] > lock2[1] - size*10) and (anom2[1] < lock2[1] + size*10) or (
        anom2[0] > lock3[0] - size*10) and (anom2[0] < lock3[0] + size*10) and (anom2[1] > lock3[1] - size*10) and (anom2[1] < lock3[1] + size*10):
        pygame.draw.rect(sc, pygame.Color('red'), (*anom2, size, size))

    if (anom3[0] > lock1[0] - size*10) and (anom3[0] < lock1[0] + size*10) and (anom3[1] > lock1[1] - size*10) and (anom3[1] < lock1[1] + size*10) or (
        anom3[0] > lock2[0] - size*10) and (anom3[0] < lock2[0] + size*10) and (anom3[1] > lock2[1] - size*10) and (anom3[1] < lock2[1] + size*10) or (
        anom3[0] > lock3[0] - size*10) and (anom3[0] < lock3[0] + size*10) and (anom3[1] > lock3[1] - size*10) and (anom3[1] < lock3[1] + size*10):
        pygame.draw.rect(sc, pygame.Color('red'), (*anom3, size, size))

    if (anom4[0] > lock1[0] - size*10) and (anom4[0] < lock1[0] + size*10) and (anom4[1] > lock1[1] - size*10) and (anom4[1] < lock1[1] + size*10) or (
        anom4[0] > lock2[0] - size*10) and (anom4[0] < lock2[0] + size*10) and (anom4[1] > lock2[1] - size*10) and (anom4[1] < lock2[1] + size*10) or (
        anom4[0] > lock3[0] - size*10) and (anom4[0] < lock3[0] + size*10) and (anom4[1] > lock3[1] - size*10) and (anom4[1] < lock3[1] + size*10):
        pygame.draw.rect(sc, pygame.Color('red'), (*anom4, size, size))

    if (anom5[0] > lock1[0] - size*10) and (anom5[0] < lock1[0] + size*10) and (anom5[1] > lock1[1] - size*10) and (anom5[1] < lock1[1] + size*10) or (
        anom5[0] > lock2[0] - size*10) and (anom5[0] < lock2[0] + size*10) and (anom5[1] > lock2[1] - size*10) and (anom5[1] < lock2[1] + size*10) or (
        anom5[0] > lock3[0] - size*10) and (anom5[0] < lock3[0] + size*10) and (anom5[1] > lock3[1] - size*10) and (anom5[1] < lock3[1] + size*10):
        pygame.draw.rect(sc, pygame.Color('red'), (*anom5, size, size))






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surf.blit(title1, (1250, 50))
    surf.blit(t1, (1300, 50))
    surf.blit(title2, (1250, 150))
    surf.blit(t2, (1300, 150))
    surf.blit(title3, (1250, 250))
    surf.blit(t3, (1300, 250))

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1
        x += dx * size
        y += dy * size
    if key[pygame.K_s]:
        dx, dy = 0, 1
        x += dx * size
        y += dy * size
    if key[pygame.K_a]:
        dx, dy = -1, 0
        x += dx * size
        y += dy * size
    if key[pygame.K_d]:
        dx, dy = 1, 0
        x += dx * size
        y += dy * size

    pygame.display.flip()
    clock.tick(fps)
#