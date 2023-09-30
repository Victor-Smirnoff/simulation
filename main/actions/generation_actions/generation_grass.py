from main.actions.generation_actions.generation_action import EntityGenerateAction
from main.entities.grass import Grass


class GrassGenerateAction(EntityGenerateAction):
    """
    Класс для генерации травы Grass
    """

    def __init__(self, worldmap, percent, type_entity=Grass):
        """
        :param worldmap: объект карты мира
        :param percent: процент заполнения карты объектами класса Grass
        """
        super().__init__(worldmap, percent, type_entity)
        self.current_percent = self.worldmap.get_current_percent_of_type_entity(self.type_entity)

    def perform(self):
        """
        Метод, вызывающий генерацию травы Grass
        """
        super().perform()

    def create_entity(self, y, x):
        """
        Метод умеет создавать объекты класса Grass по заданным координатам
        :param y: координата y
        :param x: координата x
        :return: объект класса Grass
        """
        return Grass(y, x)