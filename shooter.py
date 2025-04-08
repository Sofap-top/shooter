from pygame import*
from random import randint
font.init()
f1 = font.Font(None,30)
w = display.set_mode((700,500))
display.set_caption('Shooter')
a = transform.scale(image.load('galaxy.jpg'),(700,500))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.7)
mixer.music.play()
l = 0
o = 0
class Spr(sprite.Sprite): 
    def __init__(self,image_pic, x, y,speed=7,w=70,h=100):
        super().__init__()
        self.image = transform.scale(image.load(image_pic),(w,h))
        self.speed = speed 
        self.dir = 'right'
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ret(self):
        w.blit(self.image, (self.rect.x, self.rect.y))
class Player(Spr):
    def update(self):
        k = key.get_pressed()
        if k[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5
        if k[K_RIGHT] and self.rect.x < 635:
            self.rect.x += 5
    def fire(self):
        r = Pula('bullet.png', self.rect.centerx,self.rect.top,10,15,20)
        puli.add(r)
class Enemy(Spr):
    def update(self):
        self.rect.y += self.speed
        global l
        if self.rect.y >= 500:
            l += 1
            self.rect.y = 0
            self.rect.x = randint(70,640)
class Pula(Spr):
    def update(self):
        self.rect.y -= 12
        if self.rect.y < 0:
            self.kill()
c = time.Clock()
rocket = Player('rocket.png',250,410)
monsters = sprite.Group()
puli = sprite.Group()
for i in range(5):
    n = Enemy('asteroid.png',randint(70,640),0,4,62,62)
    monsters.add(n)
m = mixer.Sound('fire.ogg')
f = False
b = True
while b:
    if f != True:
        w.blit(a,(0,0))
        rocket.update()
        rocket.ret()
        monsters.update()
        monsters.draw(w)
        puli.update()
        puli.draw(w)
        k = f1.render('Пропущено: '+ str(l),1,(196, 184, 183) )
        w.blit(k,(10,20))
        k1 = f1.render('Счёт: '+ str(o),1,(196, 184, 183) )
        w.blit(k1,(10,45))
        z = sprite.groupcollide(monsters,puli,True,True)
        for i in z:
            o += 1 
            n = Enemy('asteroid.png',randint(70,640),0,7,62,62)
            monsters.add(n)
        if k == 5:
            f = True
            w.blit(a,(0,0))
            win = f1.render('YOU LOSE!',True,(250, 149, 7))
            w.blit(win,(200,200))
        if k1 == 25:
            f = True
            w.blit(a,(0,0))
            win1 = f1.render('YOU WIN!',True,(250, 149, 7))
            w.blit(win1,(200,200))
        if sprite.spritecollide(rocket, monsters,False):
            f = True
            w.blit(a,(0,0))
            win2 = f1.render('YOU LOSE!',True,(250, 149, 7))
            w.blit(win2,(200,200))   
    for i in event.get():
        if i.type == QUIT:
            b = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                rocket.fire() 
         
    display.update()
    c.tick(60)
