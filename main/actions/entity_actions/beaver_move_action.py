from main.entities.beaver import Beaver
from main.actions.entity_actions.move_action import MoveAction


class BeaverMoveAction(MoveAction):
    """
    Класс для описания движения Beaver
    """
    def __init__(self, worldmap, type_entity=Beaver):
        """
        Инициализатор класса движения Beaver
        :param worldmap: карта, на которой происходят действия
        :param type_entity: тип перемещаемого объекта Beaver
        """
        super().__init__(worldmap, type_entity)

    def perform(self, entity):
        """
        Метод для движения одного существа Beaver
        """
        super().perform(entity)