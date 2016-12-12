import pygame
from pygame.locals import *
import random
import math

def uus_toru():
    gapY = random.randrange(0, int(404.48 * 0.6 - 90))
    gapY += int(404.48 * 0.2)
    pipeHeight = 320
    pipeX = 800 + 10

    return [
        {'x': pipeX, 'y': gapY - pipeHeight},  # upper pipe
        {'x': pipeX, 'y': gapY + 75},  # lower pipe
    ]

def hype(aste):
    osahype = aste / float(20)
    return (1 - math.cos(osahype * math.pi)) * 5

pygame.init()
screen = pygame.display.set_mode((800, 512))
images = ("Images/background-day.png", "Images/base.png", "Images/pipe-green.png", "Images/bluebird-midflap.png")
helid = ("Audio/die.wav", "Audio/point.wav", "Audio/wing.wav")
surm_heli = pygame.mixer.Sound(helid[0])
punkt_heli = pygame.mixer.Sound(helid[1])
hüpe_heli = pygame.mixer.Sound(helid[2])

ylemised = []
alumised = []
taimer = 75
x_baas = 0
astmeid = 0
linnu_x = 75
linnu_y = 200
kukkumine = 3
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            astmeid += 12
            hüpe_heli.play()

    screen.fill((0, 0, 0))
    taust = pygame.image.load(images[0]).convert_alpha()
    for i in range(3):
        screen.blit(taust, (i*288, 0))

    for toru in ylemised:
        if toru["x"] <= -52:
            ylemised.remove(toru)
        else:
            toru["x"] -= 2

    for toru in alumised:
        if toru["x"] <= -52:
            alumised.remove(toru)
        else:
            toru["x"] -= 2

    if taimer == 75:
        taimer = 0
        uus = uus_toru()
        ylemised.append(uus[0])
        alumised.append(uus[1])

    torud_all = pygame.image.load(images[2]).convert_alpha()
    torud_yleval = pygame.transform.rotate(torud_all, 180)
    for toru in ylemised:
        screen.blit(torud_yleval, (toru["x"], toru["y"]))
    for toru in alumised:
        screen.blit(torud_all, (toru["x"], toru["y"]))


    if astmeid > 0:
        linnu_y -= hype(astmeid)
        astmeid -= 1
    else:
        linnu_y += kukkumine

    lind = pygame.image.load(images[3]).convert_alpha()
    screen.blit(lind, (linnu_x, linnu_y))

    if x_baas == 336:
        x_baas = 0

    baas = pygame.image.load(images[1]).convert_alpha()
    for i in range(4):
        screen.blit(baas, (i*336 - x_baas, 400))

    x_baas += 2
    taimer += 1
    pygame.display.flip()

    if linnu_y < 0:
        pygame.quit()
    elif linnu_y > 376:
        pygame.quit()
    for toru in alumised:
        if toru["x"] in range(23, 109) and (int(linnu_y) in range(0, toru["y"]-90) or int(linnu_y) in range(toru["y"] , 512)):
            surm_heli.play()
            pygame.quit()



pygame.quit()