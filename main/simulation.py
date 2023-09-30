from main.actions.entity_actions.beaver_eat_action import BeaverEatAction
from main.actions.entity_actions.beaver_move_action import BeaverMoveAction
from main.actions.generation_actions.generation_beaver import BeaverGenerateAction
from main.actions.generation_actions.generation_grass import GrassGenerateAction
from main.actions.generation_actions.generation_rock import RockGenerateAction
from main.actions.generation_actions.generation_tree import TreeGenerateAction
from main.actions.generation_actions.generation_herbivore import HerbivoreGenerateAction
from main.actions.generation_actions.generation_predator import PredatorGenerateAction
from main.entities.beaver import Beaver
from main.entities.herbivore import Herbivore
from main.actions.entity_actions.herbivore_eat_action import HerbivoreEatAction
from main.actions.entity_actions.herbivore_move_action import HerbivoreMoveAction
from main.entities.predator import Predator
from main.actions.entity_actions.predator_eat_action import PredatorEatAction
from main.actions.entity_actions.predator_move_action import PredatorMoveAction


class Simulation:
    """
    Класс для симуляции игрового поля
    """
    def __init__(self, worldmap, per_Gras, per_Tree, per_Rock, per_Herb, per_Pred, per_Beav):
        """
        Инициализатор класса симуляции
        :param worldmap: карта
        :param per_Gras: процент травы на карте
        :param per_Tree: процент деревьев на карте
        :param per_Rock: процент камней на карте
        :param per_Herb: процент травоядных на карте
        :param per_Pred: процент хищников на карте
        :param per_Beav: процент бобров на карте
        """
        self.worldmap = worldmap
        self.move_counter = 0
        self.stop_simulation = True
        self.per_Gras = per_Gras
        self.per_Tree = per_Tree
        self.per_Rock = per_Rock
        self.per_Herb = per_Herb
        self.per_Pred = per_Pred
        self.per_Beav = per_Beav
        # создаем список первоначальных действий lst_init_actions
        self.lst_init_actions = self.get_lst_init_actions()
        self.init_actions()

    def init_actions(self):
        """
        Метод для начальной инициализации поля
        Расставляет объекты на карте
        :return: None
        """
        # проходимо по списку действий и выполняем их все по очереди
        for pre_start_action in self.lst_init_actions:
            pre_start_action.perform()

    def get_lst_init_actions(self):
        """
        Метод создает список первоначальных действий lst_init_actions
        :return: список первоначальных действий lst_init_actions
        Этот список содержит действия по генерации:
        0 - GrassGenerateAction
        1 - RockGenerateAction
        2 - TreeGenerateAction
        3 - HerbivoreGenerateAction
        4 - PredatorGenerateAction
        5 - BeaverGenerateAction
        Объекты этого списка будут использоваться ещё для поддержания баланса количества существ на карте
        """
        lst_init_actions = [GrassGenerateAction(self.worldmap, self.per_Gras),
                        RockGenerateAction(self.worldmap, self.per_Rock),
                        TreeGenerateAction(self.worldmap, self.per_Tree),
                        HerbivoreGenerateAction(self.worldmap, self.per_Herb),
                        PredatorGenerateAction(self.worldmap, self.per_Pred),
                        BeaverGenerateAction(self.worldmap, self.per_Beav)
                        ]
        return lst_init_actions

    def turn_actions(self):
        """
        Метод для выполнения действий каждый ход: сделать ходы всеми существами, добавить существ
        Проверка количества травы. Если травы меньше определенного rate, то добавить травы
        Проверка количества травоядных. Если травоядных меньше определенного rate, то добавить травоядных
        Проверка ближайших целей еды для травоядных и для хищников
        Если ближайшие цели находятся рядом, то необходимо их атаковать
        Если целей рядом нет, то необходимо сделать ход в сторону ближайшей цели
        Количество ходов каждым существом определяется по параметру entity.speed
        :return: None
        """
        # создаем список всех существ Creature кто будет ходить
        lst_of_creatures = self.create_lst_of_creatures()

        # создаем объекты для выполнения действий
        # объекты для выполнения поедания
        objects_eat_actions = {Herbivore: HerbivoreEatAction(self.worldmap, Herbivore),
                               Predator: PredatorEatAction(self.worldmap, Predator),
                               Beaver: BeaverEatAction(self.worldmap, Beaver)
                               }

        # объекты для выполнения движения
        objects_move_actions = {Herbivore: HerbivoreMoveAction(self.worldmap, Herbivore),
                                Predator: PredatorMoveAction(self.worldmap, Predator),
                                Beaver: BeaverMoveAction(self.worldmap, Beaver)
                                }

        # берем одно существо и будем выполнять им ходы
        for creature in lst_of_creatures:
            obj_eat_action = objects_eat_actions[type(creature)]  # выбираем объект для выполнения поедания
            obj_move_action = objects_move_actions[type(creature)]  # выбираем объект для выполнения движения
            creature.make_step(creature, obj_eat_action, obj_move_action)  # выполняем ход/ходы существом

            # если после выполнения ходов у сущности стало количество здоровья равно 0, то удалить сущность с карты
            if creature.health == 0:
                self.worldmap.delete_entity(creature.y, creature.x)

        # добавляем сущности на карту, если это требуется
        self.maintain_quantity_balance_action()

    def create_lst_of_creatures(self):
        """
        Метод для создания списка всех сущностей, которые будут совершать ходы
        :return: lst_of_creatures - список сущностей
        """
        lst_of_herbovores = self.worldmap.get_list_entities(Herbivore)
        lst_of_predators = self.worldmap.get_list_entities(Predator)
        lst_of_creatures = lst_of_herbovores + lst_of_predators
        return lst_of_creatures

    def maintain_quantity_balance_action(self):
        """
        Метод выполняет поддержание баланса существ на карте
        Проверяет сколько ходов было выполнено, проверяет количество сущностей, добавляет сущности на карту
        :return: None
        """
        # каждые 3 хода будем проверять количество травоядных и генерировать Herbivore до self.per_Herb
        if not self.move_counter % 3:
            self.lst_init_actions[3].perform()  # добавляем на карту Herbivore
            self.worldmap.show_map()

        # каждые 5 ходов будем проверять количество травы и генерировать Grass до self.per_Gras
        if not self.move_counter % 5:
            self.lst_init_actions[0].perform()  # добавляем на карту Grass
            self.worldmap.show_map()

        # каждые 8 ходов будем проверять количество деревьев и генерировать Tree до self.per_Tree
        if not self.move_counter % 8:
            self.lst_init_actions[2].perform()  # добавляем на карту Tree
            self.worldmap.show_map()

        # каждые 10 ходов будем проверять количество бобров и генерировать Beaver до self.per_Beav
        if not self.move_counter % 10:
            self.lst_init_actions[5].perform()  # добавляем на карту Beaver
            self.worldmap.show_map()

        # каждые 50 ходов будем проверять количество хищников и генерировать Predator до self.per_Pred
        if not self.move_counter % 50:
            self.lst_init_actions[4].perform()  # добавляем на карту Predator
            self.worldmap.show_map()

    def render(self):
        """
        Метод для отображения количества ходов и карты в консоли
        :return: None
        """
        print(f"Счётчик ходов: {self.move_counter}")
        self.worldmap.show_map()

    def start_simulation(self):
        while self.stop_simulation:
            self.next_turn()

    def pause_simulation(self):
        self.stop_simulation = False

    def next_turn(self):
        """
        Метод для выполнения хода всеми существами
        :return: None
        """
        # каждый ход добавляем 1 к счетчику ходов
        self.move_counter += 1
        # вызываем действия по поеданию, передвижению и генерации существ
        self.turn_actions()
        # вызываем рендер для отображения текущего состояния карты в консоли
        self.render()