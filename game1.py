import pygame as pg

pg.init()
screen = pg.display.set_mode([500,500])

xa=10
ya=10
wa=30
ha=30
sp = 5
am = 10

def draw_grid(surface,color,x,y,w,h,n):
    for i in range(n):
        pg.draw.rect(surface,color,(x,y,w,h))



run = True
while run:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            run = False

    screen.fill((255,255,255)) 
    draw_grid(screen,(0,0,0),xa,ya,wa,ha,am)
    
    pg.display.update()
