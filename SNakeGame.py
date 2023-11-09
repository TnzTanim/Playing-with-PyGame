import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Set up the colors
white = (255,255,255,)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up the game variables
snake_block_size = 10
snake_speed = 15
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.SysFont(None, 25)


# Define the function to display the score
def display_score(score):
    text = font.render("Score: "+str(score), True, white)
    window.blit(text, [0, 0])

# Define the function to draw the snake
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block_size, snake_block_size])

# Define the main game function
def gameLoop():
    game_over = False
    game_close = False

    # Set up the snake's starting position and lengthq
    snake_list = []
    length_of_snake = 1
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0

    # Set up the apple's starting position
    apple_x = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
    apple_y = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0

    # Start the game loop
    while not game_over:
        while game_close == True:
            window.fill(white)
            game_over_message = font.render("Game Over!", True, red)
            window.blit(game_over_message, [window_width/3, window_height/3])
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Check if the snake goes out of bounds
        if x1 >= window_width or x1 < 0 or y1 >= window_height or  y1 < 0:
            game_close = True

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change

        # Draw the apple
        pygame.draw.rect(window, red, [apple_x, apple_y, snake_block_size, snake_block_size])

        # Draw the snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block_size, snake_list)
        display_score(length_of_snake - 1)
        pygame.display.update()

        # Check if the snake has hit the apple
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
            apple_y = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0
            length_of_snake += 1

        # Set up the game clock
        clock.tick(snake_speed)

        # Quit Pygame
    pygame.quit()

    # Call the game loop function
gameLoop()