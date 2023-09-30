class Map:
    """
    Класс для описания карты мира
    """

    def __init__(self, height, width):
        """
        Класс карты принимающий на вход два параметра
        :param height: количество клеток по высоте
        :param width: количество клеток по ширине
        """
        self.height = height
        self.width = width
        self.quantity_cells = self.height * self.width
        self.__worldmap_field = {} # словарь для представления карты,
        # ключи - это кортежи из координат (y, x), значения - объекты

    def __getitem__(self, key):
        if type(key) == tuple and 0 <= key[0] < self.height and 0 <= key[1] < self.width:
            return self.__worldmap_field[key]

    def __setitem__(self, key, value):
        if type(key) == tuple and 0 <= key[0] < self.height and 0 <= key[1] < self.width:
            self.__worldmap_field[key] = value

    def __delitem__(self, key):
        if type(key) == tuple and 0 <= key[0] < self.height and 0 <= key[1] < self.width:
            del self.__worldmap_field[key]

    def get_from_worldmap_field(self, key):
        """
        Метод для получения значения по ключу с использованием метода словаря get
        :param key: кортеж из коородинат (y, x)
        :return: возвращает значение словаря по ключу
        """
        return self.__worldmap_field.get(key)

    def get_list_all_entities(self):
        """
        Метод возвращает значения values() словаря карты self.__worldmap_field
        Метод для получения списка всех объектов сущностей на карте !
        :return: список всех объектов
        """
        return self.__worldmap_field.values()

    def get_list_entities(self, type_entity):
        """
        Метод для получения списка всех объектов одного типа
        :param type_entity: тип объекта, который требуется получить из карты
        :return: список объектов типа type_entity
        """
        return [obj for obj in self.get_list_all_entities() if type(obj) == type_entity]

    def get_entity(self, y, x):
        """
        Получить существо если оно есть в указанных координатах
        :param y: координата y
        :param x: координата x
        :return: объект существа если оно есть в указанной клетке, иначе None
        """
        return self.get_from_worldmap_field((y, x))

    def get_current_percent_of_type_entity(self, type_entity):
        """
        Метод возвращает процент заполнения карты объектами type_entity
        :return: процент тип данных число float
        """
        return (len(self.get_list_entities(type_entity)) / self.quantity_cells) * 100

    def find_empty_cells(self):
        """
        Метод для поиска всех свободных клеток на карте
        :return: список координат всех свободных клеток
        """
        return [(y, x) for y in range(self.height) for x in range(self.width) if self.is_cell_empty(y, x)]

    def is_cell_empty(self, y, x):
        """
        Метод для определения пустая ячейка или нет
        :param y: координата y
        :param x: координата x
        :return: True - пустая, False - не пустая
        """
        return self.get_from_worldmap_field((y, x)) is None

    def place_entity(self, y, x, obj):
        """
        Метод устанавливает объект на карту
        :param y: координата y
        :param x: координата x
        :param obj: объект сущности
        :return: None
        """
        self.__worldmap_field[(y, x)] = obj

    def delete_entity(self, y, x):
        """
        Метод удаляет объект с карты
        :param y: координата y
        :param x: координата x
        :return: None
        """
        del self.__worldmap_field[(y, x)]

    def move_entity(self, new_y, new_x, obj):
        """
        Метод для перемещения существ на карте
        :param new_y: координата y куда переместить
        :param new_x: координата x куда переместить
        :param obj: объект сущности для перемещения
        :return: None
        """
        self.place_entity(new_y, new_x, obj)
        self.delete_entity(obj.y, obj.x)
        obj.make_move(new_y, new_x)

    def show_map(self):
        """
        Метод для отображения текущего состояния карты
        Просто печатает в консоль объекты карты
        :return: None
        """
        print()
        for m in range(self.height):
            for n in range(self.width):
                if self.get_from_worldmap_field((m, n)):
                    print("\t" + str(self.get_from_worldmap_field((m, n))) + "\t", end=" ")
                else:
                    print("\t" + "#" + "\t", end=" ")
            print()