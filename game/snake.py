import pygame

class Snake:
    def __init__(self, window):
        self.window = window
        self.x = 0 # Snake's x-coordinate
        self.y = 0 # Snake's y-coordinate
        self.width = 20 # Snake's width
        self.height = 20 # Snake's height
        self.color = (0,255,0) # Snake's color
    
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
        