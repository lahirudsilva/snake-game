import pygame

class Snake:
    def __init__(self, window):
        self.window = window
        self.x = 0 # Snake's x-coordinate
        self.y = 0 # Snake's y-coordinate
        self.width = 20 # Snake's width
        self.height = 20 # Snake's height
        self.color = (0,255,0) # Snake's color
        self.speed = 1 # Snake's movement speed

    def handle_input(self):
        # Get the state of all keyboard keys
        keys = pygame.key.get_pressed()

        # Check if the left arrow key is pressed
        if keys[pygame.K_LEFT]:
            # Move the snake towards the left by reducing its x-coordinate
            self.x -= self.speed

        # Check if the right arrow key is pressed
        elif keys[pygame.K_RIGHT]:
            # Move the snake towards the right by increasing its x-coordinate
            self.x += self.speed

        # Check if the up arrow key is pressed
        elif keys[pygame.K_UP]:
            # Move the snake upwards by reducing its y-coordinate
            self.y -= self.speed

        # Check if the down arrow key is pressed
        elif keys[pygame.K_DOWN]:
            # Move the snake downwards by increasing its y-coordinate
            self.y += self.speed

    def update(self):
        self.handle_input()
    
    
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
