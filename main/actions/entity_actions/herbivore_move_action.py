from main.entities.herbivore import Herbivore
from main.actions.entity_actions.move_action import MoveAction


class HerbivoreMoveAction(MoveAction):
    """
    Класс для описания движения Herbivore
    """
    def __init__(self, worldmap, type_entity=Herbivore):
        """
        Инициализатор класса движения Herbivore
        :param worldmap: карта, на которой происходят действия
        :param type_entity: тип перемещаемого объекта Herbivore
        """
        super().__init__(worldmap, type_entity)

    def perform(self, entity):
        """
        Метод для движения одного существа Herbivore
        """
        super().perform(entity)