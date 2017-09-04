import pygame as pg
from player import Player
from levels import level
from bloks import *


WIN_WIDTH = 1920
WIN_HEIGHT = 1040
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"


def main():
    pg.init()
    screen = pg.display.set_mode(DISPLAY)
    pg.display.set_caption('My first game')
    bg = pg.Surface(DISPLAY)
    bg.fill(pg.Color(BACKGROUND_COLOR))
    
    timer = pg.time.Clock()
    
    hero = Player(55,55)
    left = right = False
    up = False
    
    entities = pg.sprite.Group()
    platforms_all = []
    entities.add(hero)
    
    x = y = 0
    for row in level:
        for col in row:
            if col == '-':
                pf = Platform(x, y)
                entities.add(pf)
                platforms_all.append(pf)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0
    
        

    
    while True:
        timer.tick(35)
        for e in pg.event.get():
            if e.type == pg.QUIT:
                raise SystemExit
            
            if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
                left = True
                
            if e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
                right = True
            
            if e.type == pg.KEYUP and e.key == pg.K_RIGHT:
                right = False
                
            if e.type == pg.KEYUP and e.key == pg.K_LEFT:
                left = False
                
            if e.type == pg.KEYDOWN and e.key == pg.K_UP:
                up = True
                
            if e.type == pg.KEYUP and e.key == pg.K_UP:
                up = False            
            
        screen.blit(bg, (0,0))
        
        

        hero.update(left, right, up, platforms_all)
        entities.draw(screen)
        pg.display.update()

if __name__ == "__main__":
    main()