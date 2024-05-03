from __future__ import annotations
from itertools import combinations


class Triangle:
    """Класс треугольника"""

    def __init__(self, h1: list[int], h2: list[int], h3: list[int]):
        self.heights = [h1, h2, h3]
        self.area = 1 / 2 * abs((h2[0] - h1[0]) * (h3[1] - h1[1]) - (h3[0] - h1[0]) * (h2[1] - h1[1]))
        self.index = 0

    def __repr__(self):
        return f"T({self.heights[0]}, {self.heights[1]}, {self.heights[2]})"

    @staticmethod
    def has_intersection(first_triangle, second_triangle: Triangle) -> bool:
        """Проверяет, есть ли пересечение между двумя треугольниками"""

        first_triangle_sides = [(first_triangle.heights[i - 1], first_triangle.heights[i]) for i in range(0, 3)]
        second_triangle_sides = [(second_triangle.heights[i - 1], second_triangle.heights[i]) for i in range(0, 3)]
        # h([-1],h[0]), ([0],h[1]), ([1],h[2])

        for first_side in first_triangle_sides:
            for second_side in second_triangle_sides:
                if Triangle.__is_lines_intersect(first_side[0], first_side[1], second_side[0], second_side[1]):
                    return True

        return False

    # Вспомогательные методы для определения пересечения сторон
    @staticmethod
    def __line_tr_area(a: list[int], b: list[int], c: list[int]) -> int:
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    @staticmethod
    def __intersect(a: int, b: int, c: int, d: int) -> bool:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return max(a, c) <= min(b, d)

    @staticmethod
    def __is_lines_intersect(a: list[int], b: list[int], c: list[int], d: list[int]) -> bool:
        return (Triangle.__intersect(a[0], b[0], c[0], d[0]) and
                Triangle.__intersect(a[1], b[1], c[1], d[1]) and
                Triangle.__line_tr_area(a, b, c) * Triangle.__line_tr_area(a, b, d) <= 0 and
                Triangle.__line_tr_area(c, d, a) * Triangle.__line_tr_area(c, d, b) <= 0)


class TrianglesCombination:
    """Класс, описывающий комбинацию треугольников"""

    def __init__(self, triangles: tuple[Triangle]):
        self.triangles = triangles
        self.total_area = sum([t.area for t in triangles])

    def __repr__(self):
        return f"TC({self.triangles}, {self.total_area})"

    def has_intersections(self) -> bool:
        """Проверяет треугольники в комбинации на наличие пересечений"""

        for pair in combinations(self.triangles, 2):
            if Triangle.has_intersection(pair[0], pair[1]):
                return True

    def to_coordinates_list(self):
        """Комментарии излишни"""

        return [t.heights for t in self.triangles]
