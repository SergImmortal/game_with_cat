import pygame as pg
from player import Player
from levels import level
from bloks import *

# константы
WIN_WIDTH = 640
WIN_HEIGHT = 480
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Размер дисплея
BACKGROUND_COLOR = "#004400" # Фон
# Инициализация камеры
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)
        
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
# настройки камеры        
def camera_configuration(camera, terget_rect):
    l, t, _, _ = terget_rect
    _, _, w, h = camera
    l, t = -l +WIN_WIDTH/2, -t + WIN_HEIGHT/2
    
    l = min(0, l)
    l = max(-(camera.width-WIN_WIDTH), l)
    t = max(-(camera.height-WIN_HEIGHT), t)
    t = min (0, t)
    return Rect(l, t, w, h)


def main():
    pg.init() # инициализируем пайгейм
    screen = pg.display.set_mode(DISPLAY) # устанавливаем размер дисплея
    pg.display.set_caption('My first game') #уснанавливаем название окна
    bg = pg.Surface(DISPLAY) #создать дисплей
    bg.fill(pg.Color(BACKGROUND_COLOR))#заливка дисплея фоном
    
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
    
        
        total_level_width = len(level[0])*PLATFORM_WIDTH
        total_level_height = len(level)*PLATFORM_HEIGHT
        camera = Camera(camera_configuration, total_level_width, total_level_height)
    
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
        camera.update(hero)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
            
        pg.display.update()

if __name__ == "__main__": #если окно открыто
    main()