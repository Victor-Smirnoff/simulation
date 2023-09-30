from main.entities.creature import Creature


class Beaver(Creature):
    """
    Класс Beaver Бобёр
    Кушает деревья. Является пищей для объектов типа хищник Predator
    """

    def __init__(self, y, x, speed=1, health=100, increase=50, age=0):
        """
        Инициализатор Бобёр
        :param y: координата y
        :param x: координата x
        :param speed: скорость перемещения существ (по умолчанию равно 1)
        :param health: количество здоровья существ (по умолчанию равно 100)
        :param increase: величина увеличения здоровья для существа, которое поедает (по умолчанию равно 10)
        :param age: возраст существ (по умолчанию равно 0)
        """
        super().__init__(y, x, speed, health, increase, age)
        self.decrease = 100 # Бобёр съедает все 100 хп дерева за раз
        self.speed = 1

    def __str__(self):
        return "🐀"