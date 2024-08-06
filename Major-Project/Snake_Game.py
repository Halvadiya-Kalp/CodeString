#Snake Game

import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
light_blue = (135, 206, 250)
dark_blue = (0, 0, 139)
orange = (255, 165, 0)

# Display dimensions
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by HK')

clock = pygame.time.Clock()

snake_block = 20
initial_speed = 10

font_style = pygame.font.SysFont("arial", 40)
score_font = pygame.font.SysFont("arial", 35)

def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])

def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def display_button(message, color, rect, font_size):
    font = pygame.font.SysFont("arial", font_size)
    pygame.draw.rect(dis, color, rect)
    mesg = font.render(message, True, white)
    dis.blit(mesg, [rect[0] + (rect[2] / 2 - mesg.get_width() / 2), rect[1] + (rect[3] / 2 - mesg.get_height() / 2)])

def game_loop(scores):
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    snake_speed = initial_speed

    current_direction = 'STOP'

    while not game_over:
        while game_close:
            dis.fill(black)
            display_message(f"Game Over! Your Score: {Length_of_snake - 1}", yellow)
            
            # Display new game button with the score
            display_button(f"New Game", orange, (dis_width / 2 - 70, dis_height / 2, 140, 50), 30)
            
            pygame.display.update()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pygame.Rect(dis_width / 2 - 70, dis_height / 2, 140, 50).collidepoint(pos):
                            game_loop(scores)
                            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and current_direction != 'RIGHT':
                    x1_change = -snake_block
                    y1_change = 0
                    current_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and current_direction != 'LEFT':
                    x1_change = snake_block
                    y1_change = 0
                    current_direction = 'RIGHT'
                elif event.key == pygame.K_UP and current_direction != 'DOWN':
                    y1_change = -snake_block
                    x1_change = 0
                    current_direction = 'UP'
                elif event.key == pygame.K_DOWN and current_direction != 'UP':
                    y1_change = snake_block
                    x1_change = 0
                    current_direction = 'DOWN'

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)
        display_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            snake_speed += 1

        clock.tick(snake_speed)

    scores.append(Length_of_snake - 1)
    pygame.quit()
    quit()

def main_menu(scores):
    dis.fill(black)
    font = pygame.font.SysFont("arial", 40)
    title = font.render("Welcome to Snake Game", True, white)
    dis.blit(title, [dis_width / 2 - title.get_width() / 2, dis_height / 2 - 100])

    display_button("Start Game", orange, (dis_width / 2 - 70, dis_height / 2, 140, 50), 30)
    display_button("Quit", red, (dis_width / 2 - 70, dis_height / 2 + 60, 140, 50), 30)
    
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pygame.Rect(dis_width / 2 - 70, dis_height / 2, 140, 50).collidepoint(pos):
                    game_loop(scores)
                elif pygame.Rect(dis_width / 2 - 70, dis_height / 2 + 60, 140, 50).collidepoint(pos):
                    pygame.quit()
                    quit()

# Initialize scores and start the game
scores = []
main_menu(scores)
