from main.entities.creature import Creature


class Herbivore(Creature):
    """
    Класс травоядные
    """

    def __init__(self, y, x, speed=2, health=100, increase=10, age=0):
        """
        Инициализатор травоядных
        :param y: координата y
        :param x: координата x
        :param speed: скорость перемещения существ (по умолчанию равно 1)
        :param health: количество здоровья существ (по умолчанию равно 100)
        :param increase: величина увеличения здоровья для существа, которое поедает (по умолчанию равно 10)
        :param age: возраст существ (по умолчанию равно 0)
        """
        super().__init__(y, x, speed, health, increase, age)
        self.decrease = 100 # травоядное съедает все 100 хп травы за раз
        self.speed = 2

    def __str__(self):
        return "🐄"