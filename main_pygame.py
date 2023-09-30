# код для визуализации через pygame
import pygame
import sys
from main.entities.predator import Predator
from main.entities.herbivore import Herbivore
from main.entities.grass import Grass
from main.entities.tree import Tree
from main.entities.rock import Rock
from main.entities.beaver import Beaver
from main.simulation_pygame import SimulationPyGame
from main.map import Map


# Задаем параметры карты и объектов
map_height = 10
map_width = 10

# Создаем объект класса Map
simulation_map = Map(map_height, map_width)

# Инициализация карты, расстановка объектов
per_Gras = 5 # процент карты, который занимает Grass
per_Tree = 5 # процент карты, который занимает Tree
per_Rock = 3 # процент карты, который занимает Rock
per_Herb = 2 # процент карты, который занимает Herbivore
per_Pred = 0.5 # процент карты, который занимает Predator
per_Beav = 2 # процент карты, который занимает Beaver

# Создаем объект класса Simulation
sim = SimulationPyGame(simulation_map, per_Gras, per_Tree, per_Rock, per_Herb, per_Pred, per_Beav)

# Инициализация Pygame
pygame.init()

# Размеры окна и размеры матрицы
M = map_height
N = map_width
cell_size = 65
width = N * cell_size
height = (M + 1) * cell_size

# Создание окна
screen = pygame.display.set_mode((width, height))

# Изменение названия окна
pygame.display.set_caption("Проект Симуляция реализация на python by Victor Smirnov - v2.1")

# Цвета
black = (0, 0, 0)

# Загрузка изображения
image_herbivore = pygame.image.load("main/images/herbivore.png")
image_herbivore = pygame.transform.scale(image_herbivore, (cell_size, cell_size))

image_predator = pygame.image.load("main/images/predator.png")
image_predator = pygame.transform.scale(image_predator, (cell_size, cell_size))

image_beaver = pygame.image.load("main/images/beaver.png")
image_beaver = pygame.transform.scale(image_beaver, (cell_size, cell_size))

image_grass = pygame.image.load("main/images/grass.png")
image_grass = pygame.transform.scale(image_grass, (cell_size, cell_size))

image_rock = pygame.image.load("main/images/rock.png")
image_rock = pygame.transform.scale(image_rock, (cell_size, cell_size))

image_tree = pygame.image.load("main/images/tree.png")
image_tree = pygame.transform.scale(image_tree, (cell_size, cell_size))

# Основной цикл
running = True
while running:
    sim.next_turn()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка фона black цветом
    screen.fill(black)

    # Инициализация шрифта для текста
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Счётчик ходов: {sim.move_counter}", True, (128, 128, 128))

    # Отображение матрицы
    for m in range(M):
        for n in range(N):
            # Отображение изображения вместо прямоугольника
            if simulation_map.get_entity(m, n) is not None:
                if type(simulation_map.get_entity(m, n)) == Herbivore:
                    screen.blit(image_herbivore, (m * cell_size, n * cell_size))
                elif type(simulation_map.get_entity(m, n)) == Beaver:
                    screen.blit(image_beaver, (m * cell_size, n * cell_size))
                elif type(simulation_map.get_entity(m, n)) == Predator:
                    screen.blit(image_predator, (m * cell_size, n * cell_size))
                elif type(simulation_map.get_entity(m, n)) == Grass:
                    screen.blit(image_grass, (m * cell_size, n * cell_size))
                elif type(simulation_map.get_entity(m, n)) == Rock:
                    screen.blit(image_rock, (m * cell_size, n * cell_size))
                elif type(simulation_map.get_entity(m, n)) == Tree:
                    screen.blit(image_tree, (m * cell_size, n * cell_size))

    # Отображение текста внизу экрана
    screen.blit(text_surface, (width // 2 - cell_size * 2, height - (cell_size // 2)))

    # Обновление экрана
    pygame.display.flip()

    pygame.time.delay(650)

# Завершение Pygame
pygame.quit()

# Выход из программы
sys.exit()