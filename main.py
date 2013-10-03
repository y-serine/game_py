#coding: utf-8
import pygame
from pygame.locals import *
import sys
import codecs 
import time 
import random 
GRAB_MODE=False

class gamec(object):
    def __init__(self):
        self.SCREEN_X = 640
        self.SCREEN_Y = 480
        self.SCREEN_SIZE = (self.SCREEN_X, self.SCREEN_Y)
        self.counter=0
        pygame.init()
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE,pygame.DOUBLEBUF|pygame.HWSURFACE)
        pygame.display.set_icon(pygame.image.load("serine.bmp").convert())
        pygame.display.set_caption("window")
        pygame.event.set_grab(GRAB_MODE)
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.3)
    def execute(self):
        while True:
            self.state()
            self.event.check()
    def end(self):
        pygame.display.quit()
        sys.exit()
                    
    def __call__(self):
        self.execute()

class statec(object):
    def __init__(self):
        self.state=self.first_ini
    def __call__(self):
        self.state()
    def first_ini(self):
        self.state=self.ini
    def ini(self):
        self.state=self.play
        pygame.key.set_repeat(1,1)
    def play(self):
        game.draw()
    def ending(self):
        pygame.key.set_repeat()
        
        
class drawc(object):
    def __init__(self):pass
    def __call__(self):
        self.draw_main()
    def draw_main(self):
        self.draw_HW()
        game.tools.syncfunc()
        pygame.display.flip()
    def draw_HW(self):
        game.screen.fill((100,100,100))
        font = pygame.font.Font(None, 36)
        text = font.render("Hello World!", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = game.screen.get_rect().centerx
        textpos.centery = game.screen.get_rect().centery-20
        game.screen.blit(text, textpos)
        text = font.render(str(game.counter), 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = game.screen.get_rect().centerx
        textpos.centery = game.screen.get_rect().centery+20
        game.screen.blit(text, textpos)
class eventc(object):
    def __init__(self):pass
    def __call__(self):
        pass
    def check(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pass
                #self.end()
            elif event.type==KEYDOWN:
                if event.key == K_ESCAPE:
                    game.end()
                elif event.key == K_q:
                    game.end()
                elif event.key == K_RETURN:
                    self.control.btn_M=True
                elif event.key == K_z:
                    self.control.btn_z=True
                elif event.key == K_x:
                    self.control.btn_x=True
class controlc(object):
    def __init__(self):
        self.reset()
        self.btn=self.btnc()
        self.arr=self.arrc()
        self.all=self.btn.all+self.arr.all
    def reset(self):
        btn=self.btnc()
        self.dir_v=None
        self.dir_h=None
    def process(self):pass
    class btnc(object):
        def __init__(self):
            self.z=self.btnname()
            self.x=self.btnname()
            self.a=self.btnname()
            self.s=self.btnname()
            self.M=self.btnname()
            self.S=self.btnname()
            self.C=self.btnname()
            self.main=(self.z,self.x,self.a,self.s)
            self.sub=(self.M,self.S,self.C)
            self.all=self.main+self.sub
        def sync(self):
            for b in self.all:
                b.sync()
        def pushed(self):
            return (self.z.pushed() or self.x.pushed() or self.a.pushed() or self.s.pushed())
        class btnname(object):
            def __name__(self):
                self.incl=0
                self.value=0
            def push(self):
                self.incl=1
                self.value += 1
            def release(self):
                self.incl=0
                self.value=0
            def sync(self):
                self.value*=self.incl
                self.incl=0
            def pushed(self):
                return self.value
    class arrc(object):
        def __init__(self):
            self.up=self.arrname()
            self.down=self.arrname()
            self.left=self.arrname()
            self.right=self.arrname()
            self.vert=self.vertc()
            self.hrzn=self.hrznc()
            self.vert.keys=(self.up,self.down)
            self.hrzn.keys=(self.left,self.right)
            self.all=self.vert()+self.hrzn()
        def sync(self):
            for b in self.all:
                b.sync()
        class vertc(object):
            def __init__(self):
                self.on=False
                self.keys=None
            def __call__(self):
                return self.keys
        class hrznc(object):
            def __init__(self):
                self.on=False
                self.keys=None
            def __call__(self):
                return self.keys
        class arrname(object):
            def __name__(self):
                self.incl=0
                self.value=0
            def push(self):
                if (self.dirs()).on and self.value==0:
                    self.incl=0
                else:
                    (self.dirs()).on=True
                    self.incl=1
                    self.value += 1
            def release(self):
                if (self.dirs()).on and self.value:
                    (self.dirs()).on=False
                self.incl=0
                self.value=0
            def dirs(self):
                if self==game.control.arr.up or self ==game.control.arr.down:
                    return game.control.arr.vert
                else:
                    return game.control.arr.hrzn
            def sync(self):
                if self.incl==0:
                    self.release()
                self.incl=0
            def pushed(self):
                return self.value
            
        
class toolsc(object):
    def syncfunc(self):
        game.control.reset()
        game.counter+=1
        game.event.check()
        game.control.process()
    
game=gamec()
game.state=statec()
game.draw=drawc()
game.tools=toolsc()
game.control=controlc()
game.event=eventc()


def main():
    game()

if __name__ == "__main__":
    main()





    
