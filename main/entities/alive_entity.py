from main.entities.entity import Entity


class AliveEntity(Entity):
    """
    Класс для описания всех живых существ на карте
    """
    def __init__(self, y, x, health=100, age=0):
        """
        Инифиализация живых существ
        :param y: координата y
        :param x: координата x
        :param health: количество здоровья существ (по умолчанию равно 100)
        :param age: возраст существ (по умолчанию равно 0)
        """
        super().__init__(y, x)
        self.health = health
        self.age = age
