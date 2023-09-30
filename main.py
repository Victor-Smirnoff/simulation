from main.simulation import Simulation
from main.map import Map


# Задаем параметры карты и объектов
map_height = 10
map_width = 10

# Создаем объект класса Map
simulation_map = Map(map_height, map_width)

# Инициализация карты, расстановка объектов
per_Gras = 20 # процент карты, который занимает Grass
per_Tree = 5 # процент карты, который занимает Tree
per_Rock = 5 # процент карты, который занимает Rock
per_Herb = 5 # процент карты, который занимает Herbivore
per_Pred = 1 # процент карты, который занимает Predator
per_Beav = 1 # процент карты, который занимает Beaver

# Создаем объект класса Simulation
sim = Simulation(simulation_map, per_Gras, per_Tree, per_Rock, per_Herb, per_Pred, per_Beav)

# Показываем первоначальный вид карты
simulation_map.show_map()

steps = 40
for step in range(steps):
    sim.next_turn()