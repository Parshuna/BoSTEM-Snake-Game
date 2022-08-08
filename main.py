#Parshuna Karki
# Import libraries
import pygame
import time
import random

#game varibles
Snake_speed = 13
Snake_size = 10
food_size = 10

# Window size
window_x = 720
window_y = 480

# Defines color (rgb)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0,)
blue = pygame.Color(0,0,255,)
green = pygame.Color(0,255,0,)

# Initialize pygame
pygame.init()

# Initialize game window 
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x,window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Define snake defult position
snake_position = [window_x//2, window_y//2]

# Define first blocks of a snake body
snake_body = [[window_x//2, window_y//2]]

# Get random fruit positions
fruit_position = [random.randrange(1,(window_x//food_size)) * food_size,random.randrange(1, (window_y//food_size)) * food_size ]
food_spawn = False

# Setting default snake direction twords right
direction = 'RIGHT' # The current direction snake is going
change_to = direction # The direction I want snake to go in next

# Defult score value
score = 0
score_per_food = 10

# Function to determine if 2 blocks completely over lap
def collision_detected(block1, block2):
    # Return if x,y coordinates overlap, otherwise False
    return block1[0] == block2[0] and block1[1] == block2[1]



# Game over function: Shows some text saying game over
def game_over():
    # Create font onj
    my_font = pygame.font.SysFont('times new roman',50)

    # Create text surface for font
    game_over_surface = my_font.render('Game Over',True, red)

    # Create rectangular surface for text surface
    game_over_rect = game_over_surface.get_rect()

    # setting position of text
    game_over_rect.midtop = (window_x//2, window_y//4)

    # bilt will draw the text on the screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 3 seconds, we will stop the game
    time.sleep(3)

    # deactivate game
    pygame.quit()

    # quit the program
    quit()

# Function to keep track score
def show_score():
    # Create font object for score
    score_font = pygame.font.SysFont('times new roman',25)

    # Create the display surface obj
    score_surface = score_font.render('Score :' + str(score), True, blue)

    # Create rectangular surface
    score_rect = score_surface.get_rect()

    # blit will draw the rect on screen
    game_window.blit(score_surface, score_rect)

# Main Function

while True:
    
    #Handle key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            print(change_to)

    # If two keys are pressed simultaneously
    # we dont want the snake to move into
    if change_to == 'DOWN' and direction != 'UP':
        direction = "DOWN"
    if change_to == 'UP' and direction != 'DOWN':
        direction = "UP"
    if change_to == 'RIGHT'and direction != 'LEFT':
        direction = "RIGHT"
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
     
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= Snake_size
    if direction == 'DOWN':
        snake_position[1] += Snake_size
    if direction == 'LEFT': 
        snake_position[0] -= Snake_size
    if direction == 'RIGHT':
        snake_position[0] += Snake_size
    

    # orgin_sp [100,100]
    # new_sp [110,100]
    # Inset snake position : snake_body --> [[110,100], [100,100]]
    snake_body.insert(0,list(snake_position))
    if collision_detected(snake_position, fruit_position):
        score = score + score_per_food
        food_spawn = True
    else:
    # Remove the old snake position
        snake_body.pop()

    if food_spawn:
        fruit_position = [random.randrange(1,(window_x//food_size)) * food_size,random.randrange(1, (window_y//food_size)) * food_size ]
        food_spawn = False

    # Erase the old poitoin from the screen
    game_window.fill(black)

    # Drawing the snake at newest positon
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1],Snake_size, Snake_size))
    
    pygame.draw.rect(game_window,white, pygame.Rect(fruit_position[0],fruit_position[1], food_size, food_size) )

    # Game Over Conditions

    # If you hit any edge of the screen
    # x boundaries
    if snake_position[0] < 0 or snake_position[0] > window_x-Snake_size:
        game_over()

    # y boundaries
    if snake_position[1] < 0 or snake_position[1] > window_y-Snake_size:
        game_over()


    # If you hit yourself
    for block_position in snake_body[1:]:
        if collision_detected(snake_position, block_position):
            game_over()
    
    show_score()

    # Refresh game screen
    pygame.display.update()

    #Frame Per Second / Refresh Rate
    fps.tick(Snake_speed)


