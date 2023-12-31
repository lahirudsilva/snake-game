import pygame
from pygame import font
from game.food import Food
from game.snake import Snake

# Initialize Pygame
pygame.init()

# Setup the game window
tile_size = 25  # size of each tile in pixels
window_width = 800
window_height = 800
num_tile_x = window_width // tile_size
num_tile_y = window_height // tile_size
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Create game objects
snake = Snake(window, tile_size, (tile_size, 0))  # Pass (tile_size, 0) as the self.speed parameter
food = Food(window, tile_size)
food.generate_positions(num_tile_x, num_tile_y)  # Generate initial position for the food

# Set up the font for score display
font = pygame.font.SysFont("Poppin", 36)

# Game loop
clock = pygame.time.Clock()
fps = 10  # Specify the desired frame rate (e.g., 10 frames per second)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill((0, 0, 0))

    if not snake.game_over:
        # Update game objects
        snake.update(food)

        # Draw game objects
        snake.draw()
        food.draw()

        # Display the score
        score_text = font.render("Score: " + str(snake.score), True, (255, 255, 255))
        window.blit(score_text, (10, 10))
    else:
        # Display Game Over message
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        window.blit(game_over_text, (window_width // 2 - 100, window_height // 2 - 20))
        window.blit(restart_text, (window_width // 2 - 120, window_height // 2 + 20))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Restart the game if R key is pressed
            snake.reset()

    # Update the display
    pygame.display.update()
    clock.tick(10)  # Control the FPS of the game

# Quit the game
pygame.quit()
