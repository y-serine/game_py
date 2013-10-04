#coding: utf-8
import pygame
from pygame.locals import *
import sys
import codecs 
import time 
import random 
GRAB_MODE=False
DISABLE_X_EXIT=False

        
class direction(object):
    down="down"
    up="up"
    left="left"
    right="right"



#game body
class Gamec(object):
    #global ini
    def __init__(self):
        self.SCREEN_X = 640
        self.SCREEN_Y = 480
        self.SCREEN_SIZE = (self.SCREEN_X, self.SCREEN_Y)
        self.counter=0
        pygame.init()
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE,pygame.DOUBLEBUF|pygame.HWSURFACE)
        pygame.display.set_caption("window")
        pygame.display.set_icon(pygame.image.load("serine.png").convert())
        pygame.event.set_grab(GRAB_MODE)
        pygame.mixer.init()

    #run the game called by __call__
    def execute(self):
        while True:
            self.state()
            self.event.check()

    #exit the game   
    def end(self):
        pygame.display.quit()
        sys.exit()

    #run the game           
    def __call__(self):
        self.execute()


class Statec(object):
    def __init__(self):
        self.state=self.first_ini

    #run the set function
    def __call__(self):
        self.state()

    #called once
    def first_ini(self):
        pygame.mixer.music.set_volume(0.3)
        self.state=self.ini

    #called every time before the game starts
    def ini(self):
        self.state=self.play
        pygame.key.set_repeat(1,1)

    #temp main
    def play(self):
        game.draw()

    #called when you cleared the game
    def ending(self):
        pygame.key.set_repeat()


        
        
class Drawc(object):
    def __init__(self):pass

    #called every frame
    def __call__(self):
        self.draw_main()

    #draw func main
    def draw_main(self):
        self.draw_HW()
        game.tools.syncfunc()
        game.clock.tick(30)
        pygame.display.flip()

    #pnly writes Hello World
    def draw_HW(self):
        game.screen.fill((100,100,100))
        font = pygame.font.Font(None, 36)
        text = font.render(u"Hello World! Press ESC to exit.", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = game.screen.get_rect().centerx
        textpos.centery = game.screen.get_rect().centery-20
        game.screen.blit(text, textpos)
        text = font.render(str(game.counter), 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = game.screen.get_rect().centerx
        textpos.centery = game.screen.get_rect().centery+20
        game.screen.blit(text, textpos)

        
class Eventc(object):
    def __init__(self):
        pass
    
    def __call__(self):
        pass

    #checks the event list and passes them to the next
    def check(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                if DISABLE_X_EXIT:
                    pass
                else:
                    game.end()
            elif event.type==KEYDOWN:
                if event.key == K_ESCAPE:
                    game.end()
                elif event.key == K_q:
                    game.end()
                elif event.key == K_RETURN:
                    game.control.btn.M.push()
                elif event.key == K_z:
                    game.control.btn.z.push()
                elif event.key == K_x:
                    game.control.btn.x.push()

                    
class Controlc(object):
    def __init__(self):
        self.btn=self.Btnc()
        self.arr=self.Arrc()
        #self.reset()
        self.all=self.btn.all+self.arr.all

    #sets all zero
    def reset(self):
        self.btn.reset()
        self.arr.reset()

    #called every frame
    def process(self):
        self.btn.sync()
        self.arr.sync()


    #buttun objects
    class Btnc(object):
        def __init__(self):
            self.z=self.Btnname()
            self.x=self.Btnname()
            self.a=self.Btnname()
            self.s=self.Btnname()
            self.M=self.Btnname()
            self.S=self.Btnname()
            self.C=self.Btnname()
            self.main=(self.z,self.x,self.a,self.s)
            self.sub=(self.M,self.S,self.C)
            self.all=self.main+self.sub

        #sets all zero
        def reset(self):
            for b in self.all:
                b.reset()

        #called every frame in control
        def sync(self):
            for b in self.all:
                b.sync()

        #if any buttun is pushed or not
        def pushed(self):
            return (self.z.pushed() or self.x.pushed() or self.a.pushed() or self.s.pushed())

        
        class Btnname(object):
            def __name__(self):
                self.inc=0
                self.value=0

            #called when buttun is pushed 
            def push(self):
                self.inc=1
                self.value += 1

            #sets all zero
            def reset(self):
                self.inc=0
                self.value=0

            #called every frame
            def sync(self):
                self.value*=self.inc
                self.inc=0

            #returns how long the buttun is pushed
            def pushed(self):
                return self.value


    #arrow abjects
    class Arrc(object):
        def __init__(self):
            self.up=self.Arrnamec()
            self.down=self.Arrnamec()
            self.left=self.Arrnamec()
            self.right=self.Arrnamec()
            self.vert=self.Dirsc()
            self.hrzn=self.Dirsc()
            self.vert.keys=(self.up,self.down)
            self.hrzn.keys=(self.left,self.right)
            self.all=self.vert()+self.hrzn()

        #called every frame in control  
        def sync(self):
            for b in self.all:
                b.sync()

        #set all zero
        def reset(self):
            for b in self.all:
                b.reset()

        #disables inverse directions        
        class Dirsc(object):
            def __init__(self):
                self.on=False
                self.keys=None
                
            def __call__(self):
                return self.keys

            
        class Arrnamec(object):
            def __init__(self):
                self.incl=0
                self.value=0

            #called when this pushed
            def push(self):
                if (self.dirs()).on and self.value==0:
                    self.incl=0
                else:
                    (self.dirs()).on=True
                    self.incl=1
                    self.value += 1

            #set all zero      
            def reset(self):
                if (self.dirs()).on and self.value:
                    (self.dirs()).on=False
                self.incl=0
                self.value=0

            #returns which this belongs to
            def dirs(self):
                if self==game.control.arr.up or self ==game.control.arr.down:
                    return game.control.arr.vert
                else:
                    return game.control.arr.hrzn

            #called every frame in arr  
            def sync(self):
                if self.incl==0:
                    self.reset()
                self.incl=0

            #return how long pushed    
            def pushed(self):
                return self.value
            

class Toolsc(object):
    #methods called every frame
    def syncfunc(self):
        game.control.reset()
        game.counter+=1
        game.event.check()
        game.control.process()
        
    def make_path_picture(self,target):
        return ("img/"+target)

class Objectsc(object):
    def __init__(self):
        self.enemies=Enemiesc()
    
class Enemiesc(object):
    def __init__(self):
        self.charlist=[]
        self.set_enemy_template()

    #returns the list of enemies
    def __call__(self):
        return self.charlist

    #adds a new enemy
    def add(self,enemyname):
        self.charlist.append(self.EnemyOne(enemyname))

    def set_enemy_template(self):
        self.name.temp_enemy=self.EnemyTemplatec("serine",10,"pattern")

    class name(object):
        pass

    
    #enemy template to make new enemies
    class EnemyTemplatec(object):
        def __init__(self,name,hp_max,pattern):
            self.name=name
            self.hp_max=hp_max
            self.pattern=pattern
            self.direction=direction.down
            
        def picture_load(self):
            self.img=[]
            for i in xrange(1,9):
                img=self.name+"_"+str(i)+".png"
                self.img.append(pygame.image.load(img).convert())
                

    #class called when making a new enemy
    class EnemyOnec(EnemyTemplatec):
        def __init__(self,enemyname,item):
            self.enemyname=enemyname
            self.pattern=enemyname.pattern
            self.hp_max=enemyname.hp_max
            self.item=item
            self.hp=self.hp_max
            
        def killed(self):
            game.objects.enemies.charlist.remove(self)
            Effect.add("enemy_killed",5,1)
            del self
            
        def check(self):
            if self.hp<0:
                self.killed()

        
class Effectsc(object):
    def __init__(self):
        self.effectlist=[]

    #returns the list of enemies
    def __call__(self):
        return self.effectlist

    #adds a new enemy
    def add(self,effectname):
        self.effectlist.append(self.EffectOne(effectname))

        
    #enemy template to make new enemies
    class EffectTemplatec(object):
        def __init__(self,name,count,picnum):
            self.name=name
            self.count=count
            self.picnum=picnum
            
        def picture_load(self):
            self.img=[]
            for i in xrange(0,self.picnum-1):
                img=self.name+"_"+str(i)+".png"
                self.img.append(pygame.image.load(img).convert())
    class name(object):
        pass
                

    #class called when making a new enemy
    class EffectOnec(EffectTemplatec):
        def __init__(self,effectname):
            self.effectname=effectname
            self.count=effectname.count
            
        def sync(self):
            self.count-=1
            if self.count<0:
                game.objects.effects.effectlist.remove(self)
                del self

                

    
game=Gamec()
game.state=Statec()
game.draw=Drawc()
game.tools=Toolsc()
game.control=Controlc()
game.event=Eventc()
game.clock=pygame.time.Clock()


def main():
    game()


if __name__ == "__main__":
    main()





    
