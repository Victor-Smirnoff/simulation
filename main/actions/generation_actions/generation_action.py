from random import choice
from main.actions.action import Action


class EntityGenerateAction(Action):
    """
    Класс для генерации чего бы то ни было
    """

    def __init__(self, worldmap, percent, type_entity=None):
        """
        :param worldmap: объект карты мира
        :param percent: процент заполнения карты каким-либо Entity
        """
        super().__init__(worldmap)
        self.percent = percent
        self.current_percent = 0
        self.type_entity = type_entity

    def perform(self):
        """
        Метод, вызывающий генерацию
        """
        self.generate_entity()

    def generate_entity(self):
        """
        Метод для генерации любых существ Entity
        """
        self.current_percent = self.worldmap.get_current_percent_of_type_entity(self.type_entity)
        while self.current_percent < self.percent:
            empty_cells = self.worldmap.find_empty_cells()
            y, x = choice(empty_cells)
            self.add_entity(y, x, self.create_entity(y, x))
            self.current_percent = self.worldmap.get_current_percent_of_type_entity(self.type_entity)

    def create_entity(self, y, x):
        """
        Метод умеет создавать объекты по заданным координатам
        :param y: координата y
        :param x: координата x
        :return: obj - объект какой-либо сущности
        Метод вызывает NotImplementedError чтобы его обязательно переопределить в дочерних классах
        """
        raise NotImplementedError

    def add_entity(self, y, x, obj):
        """
        Метод для добавления существ на карту
        :param y: координата y
        :param x: координата x
        :param obj: объект
        :return: None
        """
        self.worldmap.place_entity(y, x, obj)