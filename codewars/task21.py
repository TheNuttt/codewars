# Задача 21:  вычисляет среднее арифметическое число в заданном массиве

def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(find_average([3,2,4,5,2]))