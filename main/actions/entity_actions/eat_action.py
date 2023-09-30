from random import choice
from main.actions.action import Action
from main.entities.beaver import Beaver
from main.entities.grass import Grass
from main.entities.herbivore import Herbivore
from main.entities.predator import Predator
from main.entities.tree import Tree


class EatAction(Action):
    """
    Абстрактный класс для поедания существ
    """
    def __init__(self, worldmap, type_entity=None):
        """
        Инициализатор класса поедания существ
        :param worldmap: карта, на которой происходят действия
        :param type_entity: тип объекта, который будет поедать пищу
        """
        super().__init__(worldmap)
        self.type_entity = type_entity

    def perform(self, entity):
        """
        Абстрактный метод, существующий
        для вызова всех необходимых методов для поедания
        :return: None
        """
        if self.get_lst_food_from_neighbor_cells(entity):
            self.eat_food(entity)

    def eat_food(self, entity):
        """
        Метод выполняет процесс поедания пищи существом entity
        :param entity: сущность, которая будет поедать пищу
        :return: None
        """
        # выбираем случайный объект типа food для поедания
        food = choice(self.get_lst_food_from_neighbor_cells(entity))
        self.change_health_with_food_interaction(entity, food)

    def change_health_with_food_interaction(self, entity, food):
        increase = entity.increase # величина увеличения хп для существа, которое поедает
        decrease = entity.decrease # величина уменьшения хп для существа пищи

        # проверяем чтобы хп не стало больше максимума
        if entity.health + increase >= entity.max_health:
            entity.health = entity.max_health
        else:
            entity.health += increase  # поедание добавляет <increase> хп существу

        # проверяем, что пища имеет достаточно хп, чтобы вычитать из него величину <decrease>
        # если хп равно <decrease> или меньше, то хп у пищи в результате поедания становится равно нулю
        if food.health > decrease:
            food.health -= decrease  # уменьшается хп на <decrease> у пищи
        else:
            food.health = 0
            # удаляем объект пищи с карты, т.к. объект съеден
            self.worldmap.delete_entity(food.y, food.x)

    def get_lst_food_from_neighbor_cells(self, entity):
        """
        Метод проверяет есть ли пища в соседних ячейках и добавляет её в список lst_foods
        :param entity: сущность, которая будет поедать пищу
        :return: lst_foods - список сущностей еды в соседних ячейках
        Если lst_foods пустой, значит еды рядом нет
        """
        # определяем что является едой для данного типа сущности entity.
        # food_type - кортеж и типов сущностей еды
        if type(entity) == Herbivore:
            food_type = (Grass, )
        elif type(entity) == Predator:
            food_type = (Herbivore, Beaver)
        elif type(entity) == Beaver:
            food_type = (Tree, )

        # список еды в соседних ячейках, если будем находить еду, то добавим её в этот список
        lst_foods = []

        y, x = entity.y, entity.x
        neighbor_shifts = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dy, dx in neighbor_shifts:
            new_y, new_x = y + dy, x + dx
            # проверяем что соседние ячейки не вышли за пределы поля и тип объекта в ячейке равен типу пищи
            if 0 <= new_y < self.worldmap.height and 0 <= new_x < self.worldmap.width and type(self.worldmap.get_entity(new_y, new_x)) in food_type:
                lst_foods.append(self.worldmap.get_entity(new_y, new_x))

        return lst_foods