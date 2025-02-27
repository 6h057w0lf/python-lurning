import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake and food variables
snake_block = 20
snake_speed = 15

# Initial food placement
food_x = random.randint(0, (screen_width // snake_block) - 1) * snake_block
food_y = random.randint(0, (screen_height // snake_block) - 1) * snake_block

# Snake initialization
snake_body = [[100, 50]]
snake_direction = "RIGHT"

# Score
score = 0

# Clock for controlling game speed
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Update direction based on user input
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Move the snake
    head_x, head_y = snake_body[0]
    if snake_direction == "UP":
        head_y -= snake_block
    elif snake_direction == "DOWN":
        head_y += snake_block
    elif snake_direction == "LEFT":
        head_x -= snake_block
    elif snake_direction == "RIGHT":
        head_x += snake_block

    # Check for collisions with walls
    if head_x < 0 or head_x >= screen_width or head_y < 0 or head_y >= screen_height:
        running = False

    # Check if snake eats the food
    if head_x == food_x and head_y == food_y:
        score += 10
        # Add a new segment to the snake
        snake_body.append([food_x, food_y])
        # Reposition the food
        food_x = random.randint(0, (screen_width // snake_block) - 1) * snake_block
        food_y = random.randint(0, (screen_height // snake_block) - 1) * snake_block
    else:
        # Remove the tail (snake moves without growing unless it eats food)
        snake_body.pop()

    # Check for collisions with itself
    if [head_x, head_y] in snake_body[1:]:
        running = False

    # Add the new head to the snake
    snake_body.insert(0, [head_x, head_y])

    # Update the screen
    screen.fill(WHITE)

    # Draw the food
    pygame.draw.rect(screen, RED, (food_x, food_y, snake_block, snake_block))

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], snake_block, snake_block))

    # Display the score
    font = pygame.font.Font(None, 35)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(snake_speed)

# Game over message
screen.fill(WHITE)
font = pygame.font.Font(None, 50)
game_over_text = font.render("Game Over!", True, RED)
screen.blit(game_over_text, (screen_width // 2 - 120, screen_height // 2 - 25))
pygame.display.update()
time.sleep(2)

# Terminate Pygame
pygame.quit()
