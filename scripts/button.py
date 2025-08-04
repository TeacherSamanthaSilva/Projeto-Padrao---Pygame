import pygame

class Button:

    def __init__(self, color, x, y):
        
        self.display = pygame.display.get_surface()
        self.color = color
        self.rect = pygame.Rect(x,y,250,64)

    def draw(self):
        pygame.draw.rect(self.display,self.color, self.rect)