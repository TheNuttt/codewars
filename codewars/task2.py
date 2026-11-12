# Задача 2: Возведение каждой цифры числа в квадрат, после чего их объединение 

def square_digits(num):
    squared_chars = [str(int(digit) ** 2) for digit in str(num)]
    return int("".join(squared_chars))

print(square_digits(9119))
