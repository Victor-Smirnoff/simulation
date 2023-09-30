class Action:
    """
    Базовый класс, от которого будут наследоваться все активные действия
    """

    def __init__(self, worldmap):
        """
        Инициализатор базового класса
        :param worldmap: передается объект карты мира
        """
        self.worldmap = worldmap

    def perform(self):
        """
        Абстрактный метод, существующий
        для вызова всех необходимых методов
        Генерирует исключение NotImplementedError
        чтобы во всех дочерних классах этот метод был переопределён
        """
        raise NotImplementedError