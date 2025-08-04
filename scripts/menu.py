import pygame
from scripts.animatedbg import AnimatedBg
from scripts.button import Button
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text

class Menu(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimatedBg("assets/menu/bg.png",[0,0],[0,-HEIGHT],[self.all_sprites])
        self.title = Obj("assets/menu/title.png",[436,166],[self.all_sprites])

        self.btn_play = Button("white",64,520)
        self.btn_quit = Button("white",64,600)

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
        return super().events(event)

    def update(self):
        self.bg.update()
        self.btn_play.draw()
        self.btn_quit.draw()
        return super().update()




