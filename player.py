from pygame import *
import pyganim

MOWE_SPEED = 5
WIDTH = 48
HEIGHT = 34
COLOR = '#888888'
JUMP_POWER = 12
GRAVITY = 0.45
ANIMATION_DELAY = 70
ANIM_LEFT = [("blocks/heroes/L1.png"),
             ("blocks/heroes/L2.png"),
             ("blocks/heroes/L3.png")
             ]
ANIM_RIGHT = [("blocks/heroes/R1.png"),
             ("blocks/heroes/R2.png"),
             ("blocks/heroes/R3.png")
              ]

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.yvel = 0
        self.onGround = False
        #####
        self.image.set_colorkey(Color(COLOR))
        boltAnim = []
        for anim in ANIM_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        boltAnim= []
        for anim in ANIM_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltanimRight = pyganim.PygAnimation(boltAnim)
        self.boltanimRight.play()
            
    
    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER       
        if left:
            self.xvel = -MOWE_SPEED
        ######
            self.image.fill(Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))
        elif right:
            self.xvel = MOWE_SPEED
            self.image.fill(Color(COLOR))
            self.boltanimRight.blit(self.image, (0, 0))
        elif not(left or right):
            self.xvel = 0
        if not self.onGround:
            self.yvel += GRAVITY
            
        self.onGround = False
        
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        
        self.rect.x  += self.xvel
        self.collide(self.xvel, 0, platforms)
        
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    
                if xvel < 0:
                    self.rect.left = p.rect.right
                    
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                    
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0