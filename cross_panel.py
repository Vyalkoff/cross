import pygame
import random

pygame.init()



field = [
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],

]
SCREEN_SIZE = (450, 450)
pygame.display.set_caption('Крестики - нолики')
window = pygame.display.set_mode(SCREEN_SIZE)
screen = pygame.Surface(SCREEN_SIZE)
screen.fill((255, 255, 255))

game_over = False



def draw_grid(scr):  # Отрисовка поля
    for line in range(90, 361, 90):
        pygame.draw.line(scr, (0, 0, 0), (line, 0), (line, 445), 2)
        pygame.draw.line(scr, (0, 0, 0), (0, line), (445, line), 2, )


def draw_tic_tac_toe(scr, items):  # Отрисовка крестов и нолей
    for i in range(5):
        for j in range(5):
            if items[i][j] == '0':
                pygame.draw.circle(scr, (255, 0, 0), (j * 90 + 45, i * 90 + 45), 35)
            elif items[i][j] == 'x':
                pygame.draw.line(scr, (0, 0, 255), (j * 90 + 5, i * 90 + 5), (j * 90 + 85, i * 90 + 85), 3)
                pygame.draw.line(scr, (0, 0, 255), (j * 90 + 85, i * 90 + 5), (j * 90 + 5, i * 90 + 85), 3)


def get_win_check(fd, symbol):
    flag_win = False
    for line in fd:
        if line.count(symbol) == 5:
            flag_win = True
            break
    dig_left_win = 0
    dig_right_win = 0
    for i in range(5):
        ver_win = 0
        for j in range(5):  # Проверка по вертикали
            if fd[j][i] == symbol:
                ver_win += 1
            else:
                break
        if fd[i][i] == symbol:  # Проверка по диагонале с первого верхнего значения
            dig_left_win += 1
        elif field[i][i] != symbol:
            dig_left_win = 0

        if field[i][4 - i] == symbol:  # Проверка по диагонале
            dig_right_win += 1
        elif field[i][4 - i] != symbol:
            dig_right_win = 0

        if (ver_win or dig_left_win) == 5 or dig_right_win == 5:
            flag_win = True
            break

    return flag_win


mainloop = True


while mainloop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 90][pos[0] // 90] == '':
                field[pos[1] // 90][pos[0] // 90] = 'x'
                x, y = random.randrange(5), random.randrange(5)
                while field[x][y] != "":
                    x, y = random.randrange(5), random.randrange(5)
                field[x][y] = '0'

            player_win = get_win_check(field, 'x')
            ai_win = get_win_check(field, '0')
            if player_win or ai_win:
                game_over = True
                if player_win:
                    pygame.display.set_caption('Вы победили')

                elif ai_win:
                    pygame.display.set_caption('Комп выйграл')

    draw_tic_tac_toe(screen, field)
    draw_grid(screen)
    window.blit(screen, (0, 0))
    pygame.display.update()
