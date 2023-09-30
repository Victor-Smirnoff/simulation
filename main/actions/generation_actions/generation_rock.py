from main.actions.generation_actions.generation_action import EntityGenerateAction
from main.entities.rock import Rock


class RockGenerateAction(EntityGenerateAction):
    """
    Класс для генерации камней Rock
    """

    def __init__(self, worldmap, percent, type_entity=Rock):
        """
        :param worldmap: объект карты мира
        :param percent: процент заполнения карты объектами класса Rock
        """
        super().__init__(worldmap, percent, type_entity)
        self.current_percent = self.worldmap.get_current_percent_of_type_entity(self.type_entity)

    def perform(self):
        """
        Метод, вызывающий генерацию камней Rock
        """
        super().perform()

    def create_entity(self, y, x):
        """
        Метод умеет создавать объекты класса Rock по заданным координатам
        :param y: координата y
        :param x: координата x
        :return: объект класса Rock
        """
        return Rock(y, x)