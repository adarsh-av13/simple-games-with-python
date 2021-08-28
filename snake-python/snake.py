import pygame
import random
pygame.init()
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width,display_height))
pygame.display.update()
pygame.display.set_caption('S N A K E')
clock = pygame.time.Clock()
snake_speed = 15
snake_block = 30

font_style = pygame.font.SysFont("None", 50)
font_style2 = pygame.font.SysFont("None", 40)
black = (0,0,0)
blue = (0,0,255)
bg = (27,27,39)
green = (0,255,0)
yellow = (234,217,167)
red = (255,0,0)
white = (255,255,255)
fg = (77,88,140)
cur_score = 0

def show_header():
    global cur_score
    title = font_style.render('SNAKE', True, black)
    display.blit(title, [25, 5])
    score = font_style.render('SCORE:'+str(cur_score), True, black)
    display.blit(score, [display_width-200, 5])

def draw_box():
    display.fill(bg)
    show_header()

def display_message(msg,color):
    message = font_style.render(msg, True, color)
    display.blit(message, [display_width/9, display_height/2])

def game_loop():
    global cur_score
    global snake_speed
    x = display_width / 2
    y = display_height / 2
    x_change = 0
    y_change = 0
    snake_body = []
    snake_length = 1
    foodx = round((random.randrange(0,display_width-snake_block))/10) * 10
    foody = round((random.randrange(0,display_height-snake_block))/10) * 10
    game_close = False
    game_over = False
    while not game_close:
        prev_score = cur_score
        while game_over == True:
            draw_box()
            display_message('You Lost! Press P-Play Again or Q-Quit', yellow)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    elif event.key == pygame.K_p:
                        game_loop()
            if game_close == True:
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x_change != 10:
                        x_change = -10
                        y_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x_change != -10:
                        x_change = 10
                        y_change = 0
                elif event.key == pygame.K_UP:
                    if y_change != 10:
                        y_change = -10
                        x_change = 0
                elif event.key == pygame.K_DOWN:
                    if y_change != -10:
                        y_change = 10
                        x_change = 0
        
        if x<0 or x>=display_width-30 or y<0 or y>=display_height-30:
            game_over = True
        x += x_change
        y += y_change
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        
        draw_box()
        pygame.draw.rect(display, yellow, [foodx,foody, snake_block, snake_block])
        
        for part in snake_body[:-1]:
            if part == snake_head:
                game_over = True
        
        for part in snake_body:
            pygame.draw.rect(display, fg, [part[0],part[1],snake_block,snake_block],2)
        pygame.display.update()
        if x ==  foodx and y == foody:
            foodx = round((random.randrange(0,display_width-snake_block))/10)*10
            foody = round((random.randrange(0,display_height-snake_block))/10)*10
            snake_length += 1
            cur_score += 1
        if snake_speed<60 and cur_score!=0 and cur_score != prev_score and cur_score%5==0:
            snake_speed += 1
        clock.tick(snake_speed)


game_loop()
pygame.quit()
quit()