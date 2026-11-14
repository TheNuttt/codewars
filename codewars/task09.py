# Задача 9: Преобразованиее массива с двоичным значением в целое число

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)

print(binary_array_to_number([0, 0, 1, 1]))