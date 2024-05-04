from itertools import combinations as itertools_combinations
from triangle import Triangle, TrianglesCombination
from triangles_area.parser import InputParser
from visualisation import Visualizer
def get_triangle_list(coordinates_array: list[list[int]]) -> list[list[list[int]]]:
    """
    Получает на вход массив координат точек на плоскости,
    возвращает массив вершин треугольников,
    такой, что, сумма площадей треугольников наименьшая,
    треугольники не накладываются друг на друга
    """

    result_triangles_quantity = len(coordinates_array) // 3
    all_triangles = itertools_combinations(coordinates_array, 3)
    triangles = [Triangle(*coords) for coords in all_triangles]
    triangles = list(filter(lambda x: x.area, triangles))
    triangles.sort(key=lambda x: x.area)

    # for tc_indexes in combinations(len(triangles), result_triangles_quantity):
    #     combination = []
    #     try:
    #         for index in tc_indexes:
    #             new_t = triangles[index]
    #             for t in combination:
    #                 if Triangle.has_intersection(t, new_t):
    #                     raise Exception("пересечение")
    #             combination.append(triangles[index])
    #     except Exception as e:
    #         continue
    #     else:
    #         print(sum([t.area for t in combination]))
    #         return [t.heights for t in combination]


    triangles_combinations = [
        TrianglesCombination(t) for t in itertools_combinations(triangles, result_triangles_quantity)
    ]
    triangles_combinations.sort(key=lambda x: x.total_area)

    for tc in triangles_combinations:
        if not tc.has_intersections():
            print(tc.total_area)
            return tc.to_coordinates_list()


input_data = "[[-1,-1],[1,2],[1,1],[3,1],[1,0],[-2,-1],[-3,-12],[3,19],[13,17]]"

result = get_triangle_list(InputParser.from_string(input_data, 'js_array'))
print(result)
visualizer = Visualizer(800, 800)
visualizer.visualize_triangles(result)
