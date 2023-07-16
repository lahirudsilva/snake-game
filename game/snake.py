import pygame

class Snake:
    def __init__(self, window, tile_size, speed):
        self.window = window
        self.tile_size = tile_size
        self.window_width = window.get_width()
        self.window_height = window.get_height()
        self.x = 0  # Snake's x-coordinate
        self.y = 0  # Snake's y-coordinate
        self.width = tile_size  # Snake's width
        self.height = tile_size  # Snake's height
        self.color = (0, 255, 0)  # Snake's color
        self.speed_x = speed[0]  # Snake's movement speed in the x-direction
        self.speed_y = 0  # Snake's movement speed in the y-direction
        self.body = [(self.x, self.y)]  # Snake's body segments
        self.moving = False  # Flag to indicate if the snake is currently moving
        self.move_counter = 0  # Counter to regulate snake movement
        self.score = 0  # Snake's score
        self.game_over = False

    def handle_input(self):
        # Get the state of all keyboard keys
        keys = pygame.key.get_pressed()

        if not self.moving:
            # Check if any arrow key is pressed to start moving the snake
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                self.moving = True

        if self.moving and self.move_counter == 0:
            # Check if the left arrow key is pressed
            if keys[pygame.K_LEFT] and self.speed_x != self.tile_size:  # Restrict movement within left boundary
                # Set the snake's movement speed in the x-direction
                self.speed_x = -self.tile_size
                self.speed_y = 0

            # Check if the right arrow key is pressed
            elif keys[pygame.K_RIGHT] and self.speed_x != -self.tile_size:  # Restrict movement within right boundary
                # Set the snake's movement speed in the x-direction
                self.speed_x = self.tile_size
                self.speed_y = 0

            # Check if the up arrow key is pressed
            elif keys[pygame.K_UP] and self.speed_y != self.tile_size:  # Restrict movement within top boundary
                # Set the snake's movement speed in the y-direction
                self.speed_x = 0
                self.speed_y = -self.tile_size

            # Check if the down arrow key is pressed
            elif keys[pygame.K_DOWN] and self.speed_y != -self.tile_size:  # Restrict movement within bottom boundary
                # Set the snake's movement speed in the y-direction
                self.speed_x = 0
                self.speed_y = self.tile_size

            if self.speed_x != 0:
                self.move_counter = self.tile_size // abs(self.speed_x)
            elif self.speed_y != 0:
                self.move_counter = self.tile_size // abs(self.speed_y)
            else:
                self.move_counter = 1

    def update(self, food):
        # Update the snake's position and check for collisions with the food
        self.handle_input()
        self.check_collision(food)
        if self.moving:
            self.update_position()

        if self.move_counter > 0:
            self.move_counter -= 1

    def check_collision(self, food):
        # Check if the snake's head collides with the food
        if (self.x, self.y) == (food.x, food.y):
            # Generate a new position for the food
            food.generate_positions(
                self.window_width // self.tile_size, self.window_height // self.tile_size
            )
            # Increase the snake's length
            self.body.append((self.x, self.y))
            # Increment the score
            self.score += 1

            # Return early to avoid further checks
            return

        # Check if the snake's head collides with its own body
        if (self.x, self.y) in self.body[:-1]:
            # Snake collided with itself, trigger Game Over
            self.game_over = True


    def update_position(self):
        if len(self.body) > 1:
            del self.body[0]

        # Update the head position based on the speed in the x and y directions
        self.x += self.speed_x
        self.y += self.speed_y

        # Wrap the snake's position to the opposite side if it goes out of bounds
        if self.x < 0:
            self.x = self.window_width - self.tile_size
        elif self.x >= self.window_width:
            self.x = 0

        if self.y < 0:
            self.y = self.window_height - self.tile_size
        elif self.y >= self.window_height:
            self.y = 0

        # Check if the snake's head collides with its own body
        if (self.x, self.y) in self.body[:-1]:
            # Snake collided with itself, trigger Game Over
            self.game_over = True

        # Append the new head position to the body
        self.body.append((self.x, self.y))

    
    def reset(self):
        # Reset the snake's attributes to start a new game
        self.x = 0
        self.y = 0
        self.speed_x = self.tile_size
        self.speed_y = 0
        self.body = [(self.x, self.y)]
        self.moving = False
        self.move_counter = 0
        self.score = 0
        self.game_over = False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(self.window, self.color, (segment[0], segment[1], self.width, self.height))
