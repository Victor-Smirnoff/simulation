from main.actions.generation_actions.generation_action import EntityGenerateAction
from main.entities.tree import Tree


class TreeGenerateAction(EntityGenerateAction):
    """
    Класс для генерации деревьев Tree
    """

    def __init__(self, worldmap, percent, type_entity=Tree):
        """
        :param worldmap: объект карты мира
        :param percent: процент заполнения карты объектами класса Tree
        """
        super().__init__(worldmap, percent, type_entity)
        self.current_percent = self.worldmap.get_current_percent_of_type_entity(self.type_entity)

    def perform(self):
        """
        Метод, вызывающий генерацию деревьев Tree
        """
        super().perform()

    def create_entity(self, y, x):
        """
        Метод умеет создавать объекты класса Tree по заданным координатам
        :param y: координата y
        :param x: координата x
        :return: объект класса Tree
        """
        return Tree(y, x)