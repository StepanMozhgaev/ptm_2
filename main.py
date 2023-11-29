import pygame, sys
import random

# Начальная конфигурация игры
pygame.init()
clock = pygame.time.Clock()

# Определение размеров игрового поля
width = 40 * 10
height = 40 * 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TetrisGame')



# Создание списка блоков
blocks = []

# Класс блока
class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x * 40, self.y * 40, 40, 40))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def printer(self):
        print('Hello, man!')

# Создание блока
def create_block():
    return Block(4, 0, random.choice([(255,0,0), (0,255,0), (0,0,255)]))

# Функция рисования полного ряда
def draw_full_row(row):
    for block in blocks:
        if block.y == row:
            block.color = (255,255,255)

# Проверка заполненных рядов
def check_full_rows():
    for row in range(20):
        is_full = True
        for block in blocks:
            if block.y == row:
                continue
            else:
                is_full = False
                break
        if is_full:
            draw_full_row(row)

# Удаление заполненных рядов
def remove_full_rows():
    full_rows = []
    for row in range(20):
        count = 0
        for block in blocks:
            if block.y == row:
                count += 1
        if count == 10:
            full_rows.append(row)
    for row in full_rows:
        for block in blocks:
            if block.y == row:
                blocks.remove(block)
            elif block.y < row:
                block.move(0, 1)

# Главный цикл игры
def game_loop():
    game_over = False
    current_block = create_block()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Управление блоком
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_block.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    current_block.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    current_block.move(0, 1)

        # Падение блока вниз
        if not current_block.y >= 20 - 1:
            collision = False
            for block in blocks:
                if block.x == current_block.x and block.y == current_block.y + 1:
                    collision = True
                    break
            if not collision:
                current_block.move(0, 1)
        else:
            collision = True

        # Обработка столкновений
        if collision:
            for block in blocks:
                blocks.append(block)
            blocks.append(current_block)
            check_full_rows()
            remove_full_rows()

            # Конец игры
            if current_block.y <= 1:
                game_over = True
            else:
                current_block = create_block()

        # Отрисовка блоков
        screen.fill((0,0,0))
        for block in blocks:
            block.draw()
        current_block.draw()

        pygame.display.update()
        clock.tick(5)



# Запуск игры
game_loop()
