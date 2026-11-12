# Задача 5: Вычисляет расстояние между 2-мя точками на координатной сетке путем сложения модулей ращности их координат по осям X и Y

def manhattan_distance(pointA, pointB):
    return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])

print(manhattan_distance([5, 4], [3, 2]))