import pygame  # pip install pygame
import sys

pygame.init()  # инициализация модулей пайгейма

# цвета
WHITE = (255, 255, 255)  # белый
BLACK = (0, 0, 0)  # черный

# экран
screen_width = 800  # ширина экрана в пикселях
screen_height = 600  # высота экрана в пикселях
screen = pygame.display.set_mode((screen_width, screen_height))  # создаем экран
pygame.display.set_caption("Учим Pygame")  # заголовок окна игры
screen_rect = screen.get_rect()  # снимаем с поверхности экрана прямоугольник

# игрок
player_width = 50  # ширина игрока
player_height = 100  # высота игрока
player_speed = 10  # скорость движения игрока
player_image = pygame.surface.Surface((player_width, player_height))  # картинка игрока
player_rect = player_image.get_rect()  # снимаем с игрока прямоугольник
player_rect.centerx = screen_rect.centerx  # игрок в центре экрана по X
player_rect.centery = screen_rect.centery  # игрок в центре экрана по Y

# FPS
clock = pygame.time.Clock()  # создаем часы
FPS = 60  # максимальное количество кадров в секунду

# главный цикл
game = True
while game:
    """
    Главный цикл игры продолжается, пока game не станет False.
    Цикл должен обязательно закончится обновлением дисплея,
    если выйти по break до него, то игра зависнет!
    """

    # события
    for event in pygame.event.get():  # проходим по всем событиям, которые происходят сейчас
        if event.type == pygame.QUIT:  # обработка события выхода
            game = False
        if event.type == pygame.KEYDOWN:  # нажатая клавиша (не зажатая!)
            if event.key == pygame.K_ESCAPE:  # клавиша Esc
                game = False

    # клавиши
    keys = pygame.key.get_pressed()  # собираем коды нажатых клавиш в список
    if keys[pygame.K_UP]:  # клавиша стрелка вверх
        player_rect.centery -= player_speed  # двигаем игрока вверх (в PG Y растет вниз)
    if keys[pygame.K_DOWN]:  # клавиша стрелка вниз
        player_rect.centery += player_speed  # двигаем игрока вниз
    if keys[pygame.K_LEFT]:  # клавиша стрелка влево
        player_rect.centerx -= player_speed  # двигаем игрока влево
    if keys[pygame.K_RIGHT]:  # клавиша стрелка вправо
        player_rect.centerx += player_speed  # двигаем игрока вправо

    # отрисовка
    screen.fill(BLACK)  # заливаем экран чёрным, без этого на экране остаются полосы от движения объектов
    player_image.fill(WHITE)  # заливаем картинку игрока белым
    screen.blit(player_image, (player_rect.x, player_rect.y))  # рисуем игрока на экране
    pygame.display.flip()  # обновляем экран
    clock.tick(30)  # ждем 1/FPS секунд

# после завершения главного цикла
pygame.quit()  # выгружаем модули pygame из пямяти
sys.exit()  # закрываем программу даже если модули не смогли выгрузиться
