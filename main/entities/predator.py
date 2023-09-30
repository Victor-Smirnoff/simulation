from main.entities.creature import Creature


class Predator(Creature):
    """
    Класс для описания жищников
    """
    def __init__(self, y, x, speed=3, health=100, age=0, attack_power=50):
        """
        Инициализатор жищников
        :param y: координата y
        :param x: координата x
        :param speed: скорость перемещения хищника (по умолчанию равно 2)
        :param health: количество здоровья хищника (по умолчанию равно 100)
        :param age: возраст хищника (по умолчанию равно 0)
        :param attack_power: сила атаки хищника (по умолчанию равно 50)
        """
        super().__init__(y, x, speed, health, age)
        self.decrease = attack_power # хищник будет отнимать 50 хп здоровья у травоядных
        self.increase = 15
        self.speed = 3
        self.max_health = 300

    def __str__(self):
        return "🐯"