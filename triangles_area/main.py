import random

from itertools import combinations
from triangle import Triangle, TrianglesCombination
from visualisation import Visualizer


def get_triangle_list(coordinates_array: list[list[int]]) -> list[list[list[int]]]:
    """
    Получает на вход массив координат точек на плоскости,
    возвращает массив вершин треугольников,
    такой, что, сумма площадей треугольников наименьшая,
    треугольники не накладываются друг на друга
    """

    result_triangles_quantity = len(coordinates_array) // 3
    all_triangles = combinations(coordinates_array, 3)
    triangles = [Triangle(*coords) for coords in all_triangles]
    triangles = list(filter(lambda x: x.area, triangles))
    triangles.sort(key=lambda x: x.area)
    index = 0
    for i in range(1, len(triangles)):
        if not triangles[i - 1].area == triangles[i].area:
            index += 1
        triangles[i].index = index

    triangles_combinations = [TrianglesCombination(t) for t in combinations(triangles, result_triangles_quantity)]
    triangles_combinations.sort(key=lambda x: x.total_area)

    for tc in triangles_combinations:
        if not tc.has_intersections():
            return tc.to_coordinates_list()


coordinates = []
for _ in range(9):
    x = random.randint(-20, 20)
    y = random.randint(-20, 20)
    coordinates.append([x, y])

#input_data = "[[-1,-1],[1,2],[1,1],[3,1],[1,0],[-2,-1],[-3,-12],[3,19],[13,17]]"

result = get_triangle_list(coordinates)
print(result)
visualizer = Visualizer(800, 800)
visualizer.visualize_triangles(result)
