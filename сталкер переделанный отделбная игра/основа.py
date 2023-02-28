import pygame
from pygame import Surface

from parametrs import *
import sys

pygame.init()

im = pygame.image.load('map.png')  # слово сталкер не нужно если открываешь фаил в пустой рабочей среде







for m in range(i):
    if (x <= anom[m][0] + into[m] * 5 and y <= anom[m][1] + into[m] * 5) and (
            x >= anom[m][0] - into[m] * 5 and y >= anom[m][1] - into[m] * 5):
        x, y = randrange(0, res1, size), randrange(0, res, size)


for o1 in range(o):
    for i2 in range(i):
        maxx = max(anom[i2][0], lock[o1][0])
        maxy = max(anom[i2][1], lock[o1][1])
        minx = min(anom[i2][0], lock[o1][0])
        miny = min(anom[i2][1], lock[o1][1])

        locki1.append(round(((maxx-minx)**2 + (maxy-miny)**2)**0.5))
        d=(round((into[i2]/(round(((maxx - minx) ** 2 + (maxy - miny) ** 2) ** 0.5))**2), 7))
        locki11.append(round((into[i2]/(round(((maxx - minx) ** 2 + (maxy - miny) ** 2) ** 0.5))**2), 7))
    locki2.append(locki1)
    locki.append(locki11)

print(locki2, ' растояние от лок х до anom i')
print(locki11, ' интенсивность')

surf = pygame.display.set_mode((res1 * 1.5, res))
surf.fill(pygame.Color('black'))


blue = (0, 0, 255)
st: Surface = pygame.Surface((size, size))
st.fill((255, 255, 255))
st.set_alpha(180)

sc = pygame.Surface([res1, res])
clock = pygame.time.Clock()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(
                    sc, blue, event.pos, 20)
                pygame.display.update()


    surf.blit(sc, (0, 0))
    sc.blit(im, (0, 0))
    sc.blit(st, (x, y))
    #sc.fill(pygame.Color('darkorange'))
    #sc.blit(st, (x, y))
    pygame.display.update()


    for i1 in range(i):
        pygame.draw.circle(sc, pygame.Color('red'), (anom[i1][0]+15, anom[i1][1]+15), into[i1]*5)
        #if (x <= anom[i1][0]+int0[i1]*4.6 and y <= anom[i1][1]+int0[i1]*4.6) and (x >= anom[i1][0]-int0[i1]*4.6 and y >= anom[i1][1]-int0[i1]*4.6) or (
        #        x >= res1 or x < 0 or y < 0 or y >= res
        #):




    pygame.display.flip()
    clock.tick(fps)

#
