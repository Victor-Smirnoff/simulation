from main.actions.action import Action
from main.entities.beaver import Beaver
from main.entities.grass import Grass
from main.entities.herbivore import Herbivore
from main.actions.entity_actions.pathfinder import PathFinder
from main.entities.predator import Predator
from main.entities.tree import Tree


class MoveAction(Action):
    """
    Класс для описания движения существ
    """
    def __init__(self, worldmap, type_entity=None):
        """
        Инициализатор класса движения
        :param worldmap: карта, на которой происходят действия
        :param type_entity: тип перемещаемого объекта
        """
        super().__init__(worldmap)
        self.type_entity = type_entity

    def perform(self, entity):
        """
        Абстрактный метод, существующий
        для вызова всех необходимых методов для перемещения существа
        :return: None
        """
        self.make_move(entity)

    def make_move(self, entity):
        """
        Метод принимает объект сущности и двигает его к ближайшей цели
        :param entity: объект сущности
        :return: None
        """
        # получаем список еды и путей ко всем сущностям еды
        lst_of_foods_and_paths = self.get_lst_of_foods_and_paths(entity)

        # теперь делаем сортировку списка путей и выбор одного самого короткого пути
        shortest_path = self.get_shortest_path(lst_of_foods_and_paths)
        # если путь найден и длина пути больше 1, то делаем движение
        # иначе пути нет и объект стоит на месте
        if len(shortest_path) > 1:
            new_y, new_x = shortest_path[1]
            # производим перемещение объекта сущности
            self.worldmap.move_entity(new_y, new_x, entity)

    def get_lst_of_foods_and_paths(self, entity):
        """
        Метод получает объект сущности и возвращает список еды и путей ко всем сущностям еды
        :param entity: объект сущности
        :return: список еды и путей ко всем сущностям еды
        """
        # определяем что является едой для данного типа сущности entity, делаем список всех существ еды
        if type(entity) == Herbivore:
            foods = self.worldmap.get_list_entities(Grass)
        elif type(entity) == Predator:
            foods_1 = self.worldmap.get_list_entities(Herbivore)
            foods_2 = self.worldmap.get_list_entities(Beaver)
            foods = foods_1 + foods_2
        elif type(entity) == Beaver:
            foods = self.worldmap.get_list_entities(Tree)

        # делаем список еды и путей ко всем сущностям еды
        lst_of_foods_and_paths = []

        # перебираем всю еду и добавляем пути в список lst_of_foods_and_paths
        for food in foods:
            path = self.get_path_to_food(self.worldmap, entity, food)
            lst_of_foods_and_paths.append((food, path, len(path)))

        return lst_of_foods_and_paths

    def get_shortest_path(self, lst_paths):
        """
        Метод принимает список кортежей lst_paths
        :param lst_paths: список кортежей в виде (food, path, len(path))
        :return: возвращает самый короткий путь shortest_path до ближайшей пищи
        shortest_path - список кортежей координат. если пути нет (например нет цели)
        то возвращается пустой список
        """
        if lst_paths:
            lst_paths.sort(key=lambda x: x[2])
            shortest_path = lst_paths[0][1]
            return shortest_path
        else:
            return []

    def get_path_to_food(self, worldmap, creature, food):
        """
        Метод ищет путь для объекта creature на карте worldmap к объекту food
        :param worldmap: карта объект класса Map
        :param creature: объект creature для которого ищем путь
        :param food: объект food цель для объекта creature
        :return: список кортежей координат
        """
        path_finder = PathFinder(worldmap)
        start_y, start_x = creature.y, creature.x
        target_y, target_x = food.y, food.x
        target_obj = food
        path = path_finder.find_path(start_y, start_x, target_y, target_x, target_obj)
        return path