# Задача 1: Возвращает список первых n чисел, которые делятся на x

def count_by(x, n):
    return [i * x for i in range(1, n + 1)] 

print(count_by(2, 5))
