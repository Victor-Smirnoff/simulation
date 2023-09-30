from main.actions.generation_actions.generation_action import EntityGenerateAction
from main.entities.herbivore import Herbivore


class HerbivoreGenerateAction(EntityGenerateAction):
    """
    Класс для генерации травоядных Herbivore
    """

    def __init__(self, worldmap, percent, speed=1, type_entity=Herbivore):
        """
        :param worldmap: объект карты мира
        :param percent: процент заполнения карты объектами класса Herbivore
        :param speed: скорость перемещения объектов класса Herbivore
        """
        super().__init__(worldmap, percent, type_entity)
        self.speed = speed
        self.current_percent = self.worldmap.get_current_percent_of_type_entity(self.type_entity)

    def perform(self):
        """
        Метод, вызывающий генерацию травоядных Herbivore
        """
        super().perform()

    def create_entity(self, y, x):
        """
        Метод умеет создавать объекты класса Herbivore по заданным координатам
        :param y: координата y
        :param x: координата x
        :return: объект класса Herbivore
        """
        return Herbivore(y, x, self.speed)