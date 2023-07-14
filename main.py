import pygame;
from game.food import Food
from game.snake import Snake


# Initialize Pygame
pygame.init()

# Setup the game window
window_width = 800
window_height = 800
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake Game")

#Create game objects
snake = Snake(window)
food = Food(window)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the  window
    window.fill((0,0,0))

    # Draw game objects
    snake.draw()
    food.draw()

    # update the display
    pygame.display.update()

# Quit game
pygame.quit