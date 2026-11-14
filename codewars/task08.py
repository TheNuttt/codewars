# Задача 8: Возвращает строку с подсчетом овец от 1 до n

def count_sheep(n):
    return "".join(f"{i} sheep..." for i in range(1, n + 1))

print(count_sheep(4))