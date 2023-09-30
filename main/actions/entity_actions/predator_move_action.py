from main.entities.predator import Predator
from main.actions.entity_actions.move_action import MoveAction


class PredatorMoveAction(MoveAction):
    """
    Класс для описания движения Predator
    """
    def __init__(self, worldmap, type_entity=Predator):
        """
        Инициализатор класса движения Predator
        :param worldmap: карта, на которой происходят действия
        :param type_entity: тип перемещаемого объекта Predator
        """
        super().__init__(worldmap, type_entity)

    def perform(self, entity):
        """
        Метод для движения всех Predator
        """
        super().perform(entity)