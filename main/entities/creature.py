from main.entities.alive_entity import AliveEntity


class Creature(AliveEntity):
    """
    Класс для описания животных
    """
    def __init__(self, y, x, speed=1, health=100, increase=10, age=0):
        """
        Инициализатор животных
        :param y: координата y
        :param x: координата x
        :param speed: скорость перемещения существ (по умолчанию равно 1)
        :param health: количество здоровья существ (по умолчанию равно 100)
        :param increase: величина увеличения здоровья для существа, которое поедает (по умолчанию равно 10)
        :param age: возраст существ (по умолчанию равно 0)
        """
        super().__init__(y, x, health, age)
        self.speed = speed
        self.increase = increase
        self.max_health = 200
        self.target = None

    def make_move(self, new_y, new_x):
        """
        Метод для изменения координаты у существа
        :param new_y: новая координата y
        :param new_x: новая координата x
        :return: None
        """
        self.y = new_y
        self.x = new_x

    def make_step(self, creature, obj_eat_action, obj_move_action):
        """
        Метод для выполнения хода существом
        Количество ходов зависит от скорости движения существа
        Сначала существо пробует кушать если находит еду вокруг себя
        Если еду не находит, то движется к ближайшей еде
        :param creature: существо creature, которое будет ходить
        :param obj_eat_action: объект, который отвечает за процесс поедания
        :param obj_move_action: объект, который отвечает за процесс движения
        :return: None
        """
        # возраст травоядного с каждым ходом увеличивается на 1
        self.age += 1

        for step in range(self.speed):
            # сначала существо пробует найти еду вокруг себя и если находит, то кушает
            if obj_eat_action.get_lst_food_from_neighbor_cells(creature):
                obj_eat_action.perform(creature)
            else:
                # а если еды рядом нет, то ищет её и движется к ней
                obj_move_action.perform(creature)

        self.perform_aging_of_creature(creature)

    def perform_aging_of_creature(self, creature):
        """
        Метод для выполнения старения существ
        Каждый ход здоровье существа будет уменьшаться на его возраст
        :param creature: объект существа
        :return: None
        # каждый ход у животного будет отниматься хп в зависимости от его возраста
        # если возраст 1, то отнимается 1, если возраст 2, то отнимается 2 и так далее
        # этот процесс неминуемо приведет к гибели хищника от старости
        """
        if creature.health - creature.age <= 0:
            creature.health = 0
        else:
            creature.health -= creature.age