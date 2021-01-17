import pygame as pyg
import pygame.display as display
import time
import random
pyg.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
font = pyg.font.Font('neuropol.ttf', 30)
font2 = pyg.font.Font('neuropol.ttf', 20)


display_width = 600
display_height = 600
dis = display.set_mode((display_width, display_height))
display.set_caption('Snake by Hazem')

intro_image = pyg.image.load('snake.png')

snake_block = 10
snake_speed = 15
clock = pyg.time.Clock()


def score(score):
    value = font2.render("Score: " + str(score), True, white)
    dis.blit(value, [0, 0])


def draw_snake(snake_list, snake_block):
    for x in snake_list:
        pyg.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def game_loop():
    game_over = False
    game_close = False

    x1 = display_width/2
    y1 = display_height/2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(
        155, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(
        23, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)

            mesg = font2.render('You lost!', True, white)
            dis.blit(mesg, [display_width/2 -
                            (mesg.get_width()/2), display_height/2.5])
            replay = font2.render(
                'Press Q to quit or C to play again', True, white)
            dis.blit(replay, [display_width/2 - (replay.get_width()/2),
                              display_height/2.5 + 10 + mesg.get_height()])

            display.update()

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    game_over = True
                    game_close = False

                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pyg.K_c:
                        game_loop()

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                game_over = True

            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pyg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pyg.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pyg.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(black)
        pyg.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)

        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        draw_snake(snake_list, snake_block)
        score(snake_length - 1)
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, display_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pyg.quit()
    quit()


def intro():
    close = False
    while not close:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                close = True
                break
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_SPACE:
                    game_loop()

        dis.fill(white)
        title = font.render('Snake by Hazem', True, black)

        dis.blit(title, [display_width/2 -
                         (title.get_width()/2), display_height/8 + 235])
        dis.blit(intro_image, [display_width/2 -
                               (intro_image.get_width()/2), display_height/8])
        display.update()
        clock.tick(15)


if __name__ == "__main__":
    intro()
