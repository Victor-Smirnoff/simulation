from main.actions.generation_actions.generation_action import EntityGenerateAction
from main.entities.beaver import Beaver


class BeaverGenerateAction(EntityGenerateAction):
    """
    Класс для генерации бобров Beaver
    """

    def __init__(self, worldmap, percent, speed=1, type_entity=Beaver):
        """
        :param worldmap: объект карты мира
        :param percent: процент заполнения карты объектами класса Beaver
        :param speed: скорость перемещения объектов класса Beaver
        """
        super().__init__(worldmap, percent, type_entity)
        self.speed = speed
        self.current_percent = self.worldmap.get_current_percent_of_type_entity(self.type_entity)

    def perform(self):
        """
        Метод, вызывающий генерацию травоядных Beaver
        """
        super().perform()

    def create_entity(self, y, x):
        """
        Метод умеет создавать объекты класса Beaver по заданным координатам
        :param y: координата y
        :param x: координата x
        :return: объект класса Beaver
        """
        return Beaver(y, x, self.speed)