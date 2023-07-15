import pygame
import random

class Food:
    def __init__(self, window, tile_size):
        self.window = window
        self.tile_size = tile_size
        self.x = 0  # Food's x-coordinate
        self.y = 0  # Food's y-coordinate
        self.width = tile_size  # Food's width
        self.height = tile_size  # Food's height
        self.color = (255, 0, 0)  # Food's color
    
    def generate_positions(self, max_x, max_y):
        # Generate random coordinates for the food within the window boundaries
        self.x = random.randint(0, max_x - 1) * self.tile_size
        self.y = random.randint(0, max_y - 1) * self.tile_size
     
    def draw(self):
        # Draw the food image on the window
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
