from main.actions.generation_actions.generation_action import EntityGenerateAction
from main.entities.predator import Predator


class PredatorGenerateAction(EntityGenerateAction):
    """
    Класс для генерации хищников Predator
    """

    def __init__(self, worldmap, percent, speed=2, attack_power=50, type_entity=Predator):
        """
        :param worldmap: объект карты мира
        :param percent: процент заполнения карты объектами класса Predator
        :param speed: скорость перемещения объектов класса Predator
        :param attack_power: сила атаки
        """
        super().__init__(worldmap, percent, type_entity)
        self.speed = speed
        self.attack_power = attack_power
        self.current_percent = self.worldmap.get_current_percent_of_type_entity(self.type_entity)

    def perform(self):
        """
        Метод, вызывающий генерацию хищников Predator
        """
        super().perform()

    def create_entity(self, y, x):
        """
        Метод умеет создавать объекты класса Predator по заданным координатам
        :param y: координата y
        :param x: координата x
        :return: объект класса Predator
        """
        return Predator(y, x, self.speed, self.attack_power)