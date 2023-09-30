from main.actions.entity_actions.eat_action import EatAction
from main.entities.beaver import Beaver


class BeaverEatAction(EatAction):
    def __init__(self, worldmap, type_entity=Beaver):
        """
        Инициализатор класса поедания для Beaver
        :param worldmap: карта, на которой происходят действия
        :param type_entity: тип объекта Beaver, который будет поедать пищу
        """
        super().__init__(worldmap)
        self.type_entity = type_entity

    def perform(self, entity):
        """
        Метод для вызова всех необходимых методов для поедания
        :return: None
        """
        super().perform(entity)