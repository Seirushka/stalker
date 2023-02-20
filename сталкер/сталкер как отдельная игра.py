import pygame
from math import sqrt
from parametrs import *

pygame.init()

im = pygame.image.load('map.png')  # слово сталкер не нужно если открываешь фаил в пустой рабочей среде

x, y = randrange(0, res1, size), randrange(0, res, size)

while [x, y] == anom1 or [x, y] == anom2 or [x, y] == anom3 or [x, y] == anom4 or [x, y] == anom5:
    x, y = randrange(0, res1, size), randrange(0, res, size)

# локаторы
l1 = pygame.image.load('n.png')
l2 = pygame.image.load('n2.png')
l3 = pygame.image.load('n3.png')

# поле зрения
loud1 = pygame.Surface((size*21, size*21))
loud1.fill((255, 255, 255))
loud1.set_alpha(80)

loud2 = pygame.Surface((size*21, size*21))
loud2.fill((255, 255, 255))
loud2.set_alpha(80)

loud3 = pygame.Surface((size*21, size*21))
loud3.fill((255, 255, 255))
loud3.set_alpha(80)

# шрифт и вывод данных от локаторов
font = pygame.font.SysFont('Arial', 20)
t1 = font.render(str(lock1), True, pygame.Color('darkorange'))
title1 = font.render(('лок 1'), True, pygame.Color('darkorange'))
t2 = font.render(str(lock2), True, pygame.Color('darkorange'))
title2 = font.render(('лок 2'), True, pygame.Color('darkorange'))
t3 = font.render(str(lock3), True, pygame.Color('darkorange'))
title3 = font.render(('лок 3'), True, pygame.Color('darkorange'))


st = pygame.image.load('12.png')
#chad = pygame.image.load('visual/12.png')


surf = pygame.display.set_mode((res1 * 1.5, res))
surf.fill(pygame.Color('black'))

sc = pygame.Surface([res1, res])
clock = pygame.time.Clock()


while True:
    surf.blit(sc, (0, 0))
    sc.blit(im, (0, 0))
    sc.blit(loud1, aur1)
    sc.blit(loud2, aur2)
    sc.blit(loud3, aur3)

    sc.blit(l1, lock1)
    sc.blit(l2, lock2)
    sc.blit(l3, lock3)
    sc.blit(st, (x, y))
    pygame.display.update()



    if (x == anom1[0] and y == anom1[1]) or (x == anom2[0] and y == anom2[1]) or (x == anom3[0] and y == anom3[1]) or (
            x == anom4[0] and y == anom4[1]) or (x == anom5[0] and y == anom5[1]):
        print(x, y)
        break

    if x < -1 or x > res1 - 1 or y <= 0 or y > res:
        break

    # if anom1 in s:
    #в этих условиях прописывается что если наша аномалия попадает в зону сканирования какогото из лакаторов то онк подсвечивается красным

    #1 по аномалиям

    if (anom1[0] > lock1[0] - size*10) and (anom1[0] < lock1[0] + size*11) and (anom1[1] > lock1[1] - size*11) and (
            anom1[1] < lock1[1] + size*10):

        tl1 = font.render(('(№ аномалии 1)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 50))

        pygame.draw.rect(sc, pygame.Color('red'), (*anom1, size, size))

        r = sqrt(((anom1[0] - lock1[0]) / size)**2 + ((anom1[1] - lock1[1]) / size)**2)
        int = round((int0 / r**2), 2)

        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 50))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 50))


    if (anom1[0] > lock2[0] - size*10) and (anom1[0] < lock2[0] + size*11) and (anom1[1] > lock2[1] - size*11) and (
            anom1[1] < lock2[1] + size*10):

        tl1 = font.render(('(№ аномалии 1)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 350))

        pygame.draw.rect(sc, pygame.Color('red'), (*anom1, size, size))

        r = sqrt(((anom1[0] - lock2[0]) / size)**2 + ((anom1[1] - lock2[1]) / size)**2)
        int = round((int0 / r**2), 2)

        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 350))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 350))


    if (anom1[0] > lock3[0] - size*10) and (anom1[0] < lock3[0] + size*11) and (anom1[1] > lock3[1] - size*11) and (
            anom1[1] < lock3[1] + size*10):

        tl1 = font.render(('(№ аномалии 1)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 650))

        pygame.draw.rect(sc, pygame.Color('red'), (*anom1, size, size))

        r = sqrt(((anom1[0] - lock3[0]) / size)**2 + ((anom1[1] - lock3[1]) / size)**2)
        int = round((int0 / r**2), 2)

        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 650))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 650))

    # 2

    if (anom2[0] > lock1[0] - size * 10) and (anom2[0] < lock1[0] + size * 11) and (
            anom2[1] > lock1[1] - size * 11) and (anom2[1] < lock1[1] + size * 10):
        tl1 = font.render(('(№ аномалии 2)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 70))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom2, size, size))
        r = sqrt(((anom2[0] - lock1[0]) / size)**2 + ((anom2[1] - lock1[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 70))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 70))


    if (anom2[0] > lock2[0] - size * 10) and (anom2[0] < lock2[0] + size * 11) and (
            anom2[1] > lock2[1] - size * 11) and (anom2[1] < lock2[1] + size * 10):
        tl1 = font.render(('(№ аномалии 2)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 370))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom2, size, size))
        r = sqrt(((anom2[0] - lock2[0]) / size)**2 + ((anom2[1] - lock2[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 370))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 370))


    if (anom2[0] > lock3[0] - size * 10) and (anom2[0] < lock3[0] + size * 11) and (
            anom2[1] > lock3[1] - size * 11) and (anom2[1] < lock3[1] + size * 10):
        tl1 = font.render(('(№ аномалии 2)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 670))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom2, size, size))
        r = sqrt(((anom2[0] - lock3[0]) / size)**2 + ((anom2[1] - lock3[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 670))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 670))

    #3

    if (anom3[0] > lock1[0] - size * 10) and (anom3[0] < lock1[0] + size * 11) and (
            anom3[1] > lock1[1] - size * 11) and (anom3[1] < lock1[1] + size * 10):
        tl1 = font.render(('(№ аномалии 3)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 90))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom3, size, size))
        r = sqrt(((anom3[0] - lock1[0]) / size)**2 + ((anom3[1] - lock1[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 90))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 90))


    if (anom3[0] > lock2[0] - size * 10) and (anom3[0] < lock2[0] + size * 11) and (
            anom3[1] > lock2[1] - size * 11) and (anom3[1] < lock2[1] + size * 10):
        tl1 = font.render(('(№ аномалии 3)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 390))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom3, size, size))
        r = sqrt(((anom3[0] - lock2[0]) / size)**2 + ((anom3[1] - lock2[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 390))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 390))


    if (anom3[0] > lock3[0] - size * 10) and (anom3[0] < lock3[0] + size * 11) and (
            anom3[1] > lock3[1] - size * 11) and (anom3[1] < lock3[1] + size * 10):
        tl1 = font.render(('(№ аномалии 3)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 690))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom3, size, size))
        r = sqrt(((anom3[0] - lock3[0]) / size)**2 + ((anom3[1] - lock3[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 690))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 690))

    #4

    if (anom4[0] > lock1[0] - size * 10) and (anom4[0] < lock1[0] + size * 11) and (
            anom4[1] > lock1[1] - size * 11) and (anom4[1] < lock1[1] + size * 10):
        tl1 = font.render(('(№ аномалии 4)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 110))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom4, size, size))
        r = sqrt(((anom4[0] - lock1[0]) / size)**2 + ((anom4[1] - lock1[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 110))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 110))


    if (anom4[0] > lock2[0] - size * 10) and (anom4[0] < lock2[0] + size * 11) and (
            anom4[1] > lock2[1] - size * 11) and (anom4[1] < lock2[1] + size * 10):
        tl1 = font.render(('(№ аномалии 4)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 410))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom4, size, size))
        r = sqrt(((anom4[0] - lock2[0]) / size)**2 + ((anom4[1] - lock2[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 410))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 410))


    if (anom4[0] > lock3[0] - size * 10) and (anom4[0] < lock3[0] + size * 11) and (
            anom4[1] > lock3[1] - size * 11) and (anom4[1] < lock3[1] + size * 10):
        tl1 = font.render(('(№ аномалии 4)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 710))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom4, size, size))
        r = sqrt(((anom4[0] - lock3[0]) / size)**2 + ((anom4[1] - lock3[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 710))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 710))

    #5

    if (anom5[0] > lock1[0] - size * 10) and (anom5[0] < lock1[0] + size * 11) and (
            anom5[1] > lock1[1] - size * 11) and (anom5[1] < lock1[1] + size * 10):
        tl1 = font.render(('(№ аномалии 5)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 130))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom5, size, size))
        r = sqrt(((anom5[0] - lock1[0]) / size)**2 + ((anom5[1] - lock1[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 130))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 130))


    if (anom5[0] > lock2[0] - size * 10) and (anom5[0] < lock2[0] + size * 11) and (
            anom5[1] > lock2[1] - size * 11) and (anom5[1] < lock2[1] + size * 10):
        tl1 = font.render(('(№ аномалии 5)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 430))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom5, size, size))
        r = sqrt(((anom5[0] - lock2[0]) / size)**2 + ((anom5[1] - lock2[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 430))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 430))


    if (anom5[0] > lock3[0] - size * 10) and (anom5[0] < lock3[0] + size * 11) and (
            anom5[1] > lock3[1] - size * 11) and (anom5[1] < lock3[1] + size * 10):
        tl1 = font.render(('(№ аномалии 5)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 730))
        pygame.draw.rect(sc, pygame.Color('red'), (*anom5, size, size))
        r = sqrt(((anom5[0] - lock3[0]) / size)**2 + ((anom5[1] - lock3[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 730))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 730))

    #if (anom3[0] > lock1[0] - size*10) and (anom3[0] < lock1[0] + size*10) and (anom3[1] > lock1[1] - size*10) and (anom3[1] < lock1[1] + size*10) or (
    #    anom3[0] > lock2[0] - size*10) and (anom3[0] < lock2[0] + size*10) and (anom3[1] > lock2[1] - size*10) and (anom3[1] < lock2[1] + size*10) or (
    #    anom3[0] > lock3[0] - size*10) and (anom3[0] < lock3[0] + size*10) and (anom3[1] > lock3[1] - size*10) and (anom3[1] < lock3[1] + size*10):
    #    pygame.draw.rect(sc, pygame.Color('red'), (*anom3, size, size))

    #if (anom4[0] > lock1[0] - size*10) and (anom4[0] < lock1[0] + size*10) and (anom4[1] > lock1[1] - size*10) and (anom4[1] < lock1[1] + size*10) or (
    #    anom4[0] > lock2[0] - size*10) and (anom4[0] < lock2[0] + size*10) and (anom4[1] > lock2[1] - size*10) and (anom4[1] < lock2[1] + size*10) or (
    #    anom4[0] > lock3[0] - size*10) and (anom4[0] < lock3[0] + size*10) and (anom4[1] > lock3[1] - size*10) and (anom4[1] < lock3[1] + size*10):
    #    pygame.draw.rect(sc, pygame.Color('red'), (*anom4, size, size))

    #if (anom5[0] > lock1[0] - size*10) and (anom5[0] < lock1[0] + size*10) and (anom5[1] > lock1[1] - size*10) and (anom5[1] < lock1[1] + size*10) or (
    #    anom5[0] > lock2[0] - size*10) and (anom5[0] < lock2[0] + size*10) and (anom5[1] > lock2[1] - size*10) and (anom5[1] < lock2[1] + size*10) or (
    #    anom5[0] > lock3[0] - size*10) and (anom5[0] < lock3[0] + size*10) and (anom5[1] > lock3[1] - size*10) and (anom5[1] < lock3[1] + size*10):
    #    pygame.draw.rect(sc, pygame.Color('red'), (*anom5, size, size))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surf.blit(title1, (1250, 50))
    surf.blit(t1, (1300, 50))
    surf.blit(title2, (1250, 350))
    surf.blit(t2, (1300, 350))
    surf.blit(title3, (1250, 650))
    surf.blit(t3, (1300, 650))

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1
        x += dx * size
        y += dy * size
        st = pygame.image.load('12.png')
    if key[pygame.K_s]:
        dx, dy = 0, 1
        x += dx * size
        y += dy * size
        st = pygame.image.load('12down.png')
    if key[pygame.K_a]:
        dx, dy = -1, 0
        x += dx * size
        y += dy * size
        st = pygame.image.load('12left.png')
    if key[pygame.K_d]:
        dx, dy = 1, 0
        x += dx * size
        y += dy * size
        st = pygame.image.load('12right.png')

    pygame.display.flip()
    clock.tick(fps)

#