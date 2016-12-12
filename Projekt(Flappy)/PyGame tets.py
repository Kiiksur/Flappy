import pygame as py

py.init()
esimene_aken = py.display.set_mode( (800, 600))
py.display.set_caption("Esimene aken")
esimene_aken.fill( (0,150,255) )

ristkylik1 = py.Rect(0, 0, 200, 200)
ristkylik2 = py.Rect(100, 100, 100, 100)
py.draw.rect(esimene_aken, (0, 3, 133), ristkylik1)
py.draw.rect(esimene_aken, (133, 0, 3), ristkylik2)

#pilt1 = py.image.load("Images/munn.png")
#esimene_aken.blit(pilt1, (250,150))

tekst = "Joel on kunn"
meie_font = py.font.SysFont("Arial", 72)
teksti_pilt = meie_font.render(tekst, False, (25, 25, 155))
koordinaat = 300
esimene_aken.blit(teksti_pilt, (koordinaat, 0))

py.display.flip()

while True:
    koordinaat -= 2
    if koordinaat < -50:
        koordinaat = 850
    esimene_aken.blit(teksti_pilt, (koordinaat, 0))
    py.display.flip()
while True:
    event = py.event.poll()
    if event.type == py.QUIT:
        break

py.quit()
