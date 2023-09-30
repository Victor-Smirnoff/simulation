from collections import deque


class PathFinder:
    def __init__(self, worldmap):
        """
        Конструктор класса PathFinder.

        Args:
            worldmap (Map): Карта симуляции, на которой происходит поиск пути.
        """
        self.worldmap = worldmap

    # Алгоритм BFS поиска пути в ширину
    def find_path(self, start_y, start_x, target_y, target_x, target_obj):
        """
        Метод для поиска пути с использованием алгоритма поиска в ширину (BFS).

        Args:
            start_x (int): Начальная координата X.
            start_y (int): Начальная координата Y.
            target_x (int): Целевая координата X.
            target_y (int): Целевая координата Y.

        Returns:
            list of tuple: Список кортежей с координатами пути от (start_y, start_x) до (target_y, target_x).
                          Если путь не найден, возвращается пустой список.
        """
        m = self.worldmap.height
        n = self.worldmap.width
        INF = float('inf')
        delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        d = [[INF] * n for _ in range(m)]
        p = [[None] * n for _ in range(m)]
        used = [[False] * n for _ in range(m)]
        queue = deque()

        d[start_y][start_x] = 0
        used[start_y][start_x] = True
        queue.append((start_y, start_x))
        while queue:
            y, x = queue.popleft()
            for dy, dx in delta:
                ny, nx = y + dy, x + dx
                if 0 <= ny < m and 0 <= nx < n and not used[ny][nx] and (self.worldmap.get_from_worldmap_field((ny, nx)) is None or type(self.worldmap.get_from_worldmap_field((ny, nx))) == type(target_obj)):
                    d[ny][nx] = d[y][x] + 1
                    p[ny][nx] = (y, x)
                    used[ny][nx] = True
                    queue.append((ny, nx))

        curr = (target_y, target_x)
        path = []
        while curr is not None:
            path.append(curr)
            curr = p[curr[0]][curr[1]]
        path.reverse()

        return path