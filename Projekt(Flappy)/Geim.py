import pygame
from pygame.locals import *
import random
import math
import time

def factory_reset():                                                                                                                #Põhimõtteliselt alustab mängu uuesti
    global ylemised, alumised, taimer, x_baas, astmeid, linnu_x, linnu_y, kukkumine, kukkumist, toruvahe, surm, skoor, lopu_aeg
    ylemised = []
    alumised = []
    taimer = 75
    x_baas = 0
    astmeid = 0
    linnu_x = 75
    linnu_y = 200
    kukkumine = 3
    kukkumist = 0
    toruvahe = 100
    surm = 0
    skoor = 0
    lopu_aeg = 0

def uus_toru():                                                                                                                     #Funktsioon uue toru genereerimiseks
    global toruvahe
    vahe = random.randrange(0, int(404.48 * 0.6 - toruvahe))                                                                        #Võtab suvalise vahemiku toru jaoks
    vahe += int(404.48 * 0.2)
    korgus = 320                                                                                                                    #Toru kõrgus
    asukoht = 800 + 10                                                                                                              #Paigutab toru natukene ekraanis väljapoole

    return [
        {'x': asukoht, 'y': vahe - korgus},                                                                                         #Tagastab ülemise toru
        {'x': asukoht, 'y': vahe + toruvahe},                                                                                       #Tagastab alumise toru
    ]

def hype(aste):
    osahype = aste / float(18)
    return (1 - math.cos(osahype * math.pi)) * 5                                                                                    #Arvutab kaare, et hüppamine oleks natukene sujuvam

def start():                                                                                                                        #Funktsioon, mis paneb programmi tööle
    global screen, taust, baas, x_baas, logo
    start = 0
    screen.fill((0,0,0))
    for i in range(3):
        screen.blit(taust, (i*288, 0))
        
    tekst = "Alustamiseks vajuta 'tühikut' või ülemist noolt"
    font = pygame.font.SysFont("Arial", 25)
    alustekst = font.render(tekst, True, (0,0,0))
    screen.blit(alustekst,(220, 270))

    if x_baas == 336:       
            x_baas = 0

    for i in range(4):
        screen.blit(baas, (i*336 - x_baas, 400))
    screen.blit(logo,(240,150))

    pygame.display.flip()
    while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    return start
                

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((800, 512))
images = ("Images/background-day.png", "Images/base.png", "Images/pipe-green.png", "Images/bluebird-midflap.png",
          "Images/0.png", "Images/1.png", "Images/2.png", "Images/3.png", "Images/4.png", "Images/5.png",
          "Images/6.png", "Images/7.png", "Images/8.png", "Images/9.png", "Images/gameover.png","Images/logo2.png")
helid = ("Audio/die.wav", "Audio/point.wav", "Audio/wing.wav", "Audio/hit.wav")
löök_heli = pygame.mixer.Sound(helid[3])
surm_heli = pygame.mixer.Sound(helid[0])
punkt_heli = pygame.mixer.Sound(helid[1])
hüpe_heli = pygame.mixer.Sound(helid[2])
taust = pygame.image.load(images[0]).convert_alpha()
torud_all = pygame.image.load(images[2]).convert_alpha()
torud_yleval = pygame.transform.rotate(torud_all, 180)
lind = pygame.image.load(images[3]).convert_alpha()
baas = pygame.image.load(images[1]).convert_alpha()
labi = pygame.image.load(images[14]).convert_alpha()
logo = pygame.image.load(images[15]).convert_alpha()
nr0 = pygame.image.load(images[4]).convert_alpha()
nr1 = pygame.image.load(images[5]).convert_alpha()
nr2 = pygame.image.load(images[6]).convert_alpha()
nr3 = pygame.image.load(images[7]).convert_alpha()
nr4 = pygame.image.load(images[8]).convert_alpha()
nr5 = pygame.image.load(images[9]).convert_alpha()
nr6 = pygame.image.load(images[10]).convert_alpha()
nr7 = pygame.image.load(images[11]).convert_alpha()
nr8 = pygame.image.load(images[12]).convert_alpha()
nr9 = pygame.image.load(images[13]).convert_alpha()
numbrid = [nr0, nr1, nr2, nr3, nr4, nr5, nr6, nr7, nr8, nr9]

ylemised = []
alumised = []
taimer = 75
x_baas = 0
astmeid = 0
linnu_x = 75
linnu_y = 200
kukkumine = 3
kukkumist = 0
toruvahe = 100
surm = 0
skoor = 0
lopu_aeg = 0


if start() ==0:
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):                                     #Kui vajutada ESC nuppu, siis viskab mängust välja
                pygame.quit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP) and surm == 0:                       #Hüppamise jaoks tuleb vajutada nuppu SPACE või UP
                astmeid += 12
                hüpe_heli.play()
            elif surm == 1 and event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP)\
                    and ((lopu_aeg - surma_aeg) > 2):                                                                       #Kui suremise hetkest on 2 sekundit möödas, siis saab uuesti alustada
                factory_reset()
                surm = 0

        screen.fill((0, 0, 0))                                                                                              #Teeb terve ekraani mustaks, et saaks uuesti alustada joonistamist
        for i in range(3):
            screen.blit(taust, (i*288, 0))                                                                                  #Paigutab tagumise tausta kõige esimesena kolm korda kõrvuti

        if surm == 0:                                                                                                       #Kui pole surnud, siis eemaldab torud, mis ekraanilt väljas või liigutab olemasolevaid
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

        if taimer == 75 and surm == 0:                                                                                      #Kui pole surnud, siis lisab uued torud juurde
            taimer = 0
            uus = uus_toru()
            ylemised.append(uus[0])
            alumised.append(uus[1])

        for toru in ylemised:                                                                                               #Joonistab uued torud nii üles kui ka alla
            screen.blit(torud_yleval, (toru["x"], toru["y"]))
        for toru in alumised:
            screen.blit(torud_all, (toru["x"], toru["y"]))


        if astmeid > 0:                                                                                                     #Kui on vajutatud hüppamiseks nuppu, siis arvutab mitu pikslit tuleb üles liikuda
            linnu_y -= hype(astmeid)
            kukkumine = 3
            astmeid -= 1
            if surm == 1:
                linnu_x += 2
        else:                                                                                                               #Kui ei, siis kukkumise kiirust
            kukkumine *= 1.035
            linnu_y += kukkumine
            if surm == 1:                                                                                                   #Kui oled surnud, siis liigutab edasi
                linnu_x += 2

        screen.blit(lind, (linnu_x, linnu_y))                                                                               #Joonistab linnu ekraanile

        if x_baas == 336:                                                                                                   #Vajalik maapinna liigutamiseks
            x_baas = 0

        for i in range(4):
            screen.blit(baas, (i*336 - x_baas, 400))                                                                        #Joonistab maapinna ja liigutab seda

        if surm == 0:                                                                                                       #Liigutab maapinda ainult siis, kui oled elus
            x_baas += 2
        taimer += 1

        if skoor > 99:                                                                                                      #Joonistab 3-kohalise skoori kui vajalik
            a = skoor // 100
            b = (skoor - a*100) // 10
            c = (skoor - a*100 - b*10)
            laius = numbrid[c].get_width() + numbrid[b].get_width() + numbrid[a].get_width()
            nihe = (800-laius)/2
            screen.blit(numbrid[a], (nihe, 20))
            nihe += numbrid[a].get_width()
            screen.blit(numbrid[b], (nihe, 20))
            nihe += numbrid[b].get_width()
            screen.blit(numbrid[c], (nihe, 20))

        elif skoor > 9:                                                                                                     #Joonistab 2-kohalise skoori kui vajalik
            b = skoor // 10
            c = (skoor - b*10)
            laius = numbrid[c].get_width() + numbrid[c].get_width()
            nihe = (800-laius)/2
            screen.blit(numbrid[b], (nihe, 20))
            nihe += numbrid[b].get_width()
            screen.blit(numbrid[c], (nihe, 20))

        else:                                                                                                               #Joonistab lihtsa ühekohalise skoori
            c = skoor
            laius = numbrid[c].get_width()
            screen.blit(numbrid[c], ((800-laius)/2, 20))

        if surm == 1:                                                                                                       #Kui oled surnud, siis joonistab ka "Game over" sildi
            screen.blit(labi, ((800-labi.get_width())/2, 200))
            tekst= "Uuesti mängimiseks vajuta 'tühikut' või ülemist noolt"
            font = pygame.font.SysFont("Arial", 25)
            kiri = font.render(tekst, True, (0, 0, 0))
            screen.blit(kiri, (175, 275))
            lopu_aeg = time.clock()

        pygame.display.flip()                                                                                               #Vastavalt värskendab ekraani

        if (linnu_y < 0 and surm == 0) or (linnu_y > 376 and surm == 0):                                                    #Kontrollib, kas oled lennanud vastu maad või taevast
            löök_heli.play()
            surm_heli.play()                                                                                                #Mängib vastavad helid
            astmeid += 24                                                                                                   #Lisab väikese kaarekese lõppu
            surm = 1                                                                                                        #Annab teada mängule, et oled surnud
            surma_aeg = time.clock()                                                                                        #Kontrolliks, et kaua on aega möödunud surmast
            kukkumine = 6                                                                                                   #Suurendab kukkumise kiirust

        for toru in alumised:
            if toru["x"] in range(23, 109) and (int(linnu_y) in range(0, toru["y"]-toruvahe) or int(linnu_y)\
                    in range(toru["y"]-(lind.get_height()), 512)) and surm == 0:                                            #Kontrollib kas oled vastu toru lennanud
                löök_heli.play()
                surm_heli.play()                                                                                            #Mängib vastavad helid
                astmeid += 24                                                                                               #Lisab väikse kaarekese lõppu
                surm = 1                                                                                                    #Annab teada mängule, et oled surnud
                surma_aeg = time.clock()                                                                                    #Kontrolliks, et kaua on aega möödunud surmast
                kukkumine = 6                                                                                               #Suurendab kukkumise kiirust
        if len(ylemised) >= 2 and surm == 0:
            if linnu_x + 12 in range(ylemised[0]["x"] + 25, ylemised[0]["x"] + 26) or linnu_x + 12\
                    in range(ylemised[1]["x"] + 25, ylemised[1]["x"] + 26):                                                 #Kontrollib kas oled täpselt torude vahel
                punkt_heli.play()                                                                                           #Mängib vastava heli
                skoor += 1                                                                                                  #Annab ühe punkti juurde

        time.sleep(0.0095)                                                                                                  #Magab mingi hetke, on võimalik muuta vastavalt arvuti kiirusele

