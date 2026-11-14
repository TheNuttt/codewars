# Задача 14: Возвращает 

def series_sum(n):
    total = 0.0
    for i in range(n):
        total += 1 / (1 + 3 * i)
    return f"{total:.2f}" 

print(series_sum(2))