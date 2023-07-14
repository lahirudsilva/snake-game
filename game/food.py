import pygame

class Food:
    def __init__(self, window):
        self.window = window
        self.x = 100 # Food's x-coordinate
        self.y = 100 # Food's x-coordinate
        self.width = 20 # Food's width
        self.height = 20 # Food's height
        self.color = (255, 0,0) # Food's color

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))