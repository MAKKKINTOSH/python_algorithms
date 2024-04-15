from parser import InputParser
from collections import Counter

s = "[[-1,-1],[1,2],[1,1],[3,1],[1,0],[-2,-1]]"


def get_triangle_list(coordinates_array: list[list[int]]) -> list[list[list[int]]]:
    """
    Получает на вход массив координат точек на плоскости,
    возвращает массив вершин треугольников,
    такой, что, сумма площадей треугольников наименьшая,
    треугольники не накладываются друг на друга
    """
    result = []
    coordinates_array = list(map(lambda x: x + [0], coordinates_array))
    occurrence_frequency = Counter(map(lambda x: x[0], coordinates_array))
    most_commons_x = occurrence_frequency.most_common()
    for base_x in most_commons_x:
        base_x_points = list(filter(lambda x: x[0] == base_x[0], coordinates_array))

        for coordinate in base_x_points:
            coordinates_array.remove(coordinate)





get_triangle_list(InputParser.from_string(s, "js_array"))
