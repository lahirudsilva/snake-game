import pygame;


# Initialize Pygame
pygame.init()

# Setup the game window
window_width = 800
window_height = 800
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake Game")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Clear the  window
    window.fill((0,0,0))

    #update the display
    pygame.display.update()



# Quit game
pygame.quit