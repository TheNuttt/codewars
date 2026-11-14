# Задача 7: Находит стационарное число по признаку делимости на 13

def thirt(n):
    remainders = [1, 10, 9, 12, 3, 4]
    while True:
        digits = [int(d) for d in str(n)][::-1]
        total = sum(d * remainders[i % 6] for i, d in enumerate(digits))
        if total == n:
            return total
        n = total

print(thirt(1234567))