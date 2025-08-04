import random
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text

class Game(Scene):

    def __init__(self):
        super().__init__()

    def colision(self):
        pass

    def gameover(self):
        pass
                
    def update(self):
        self.colision()
        self.gameover()
        return super().update()
