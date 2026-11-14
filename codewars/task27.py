# Задача 27: Находит наибольшее и наименьшее числа

def high_and_low(numbers):
    nums = [int(x) for x in numbers.split()]
    return f"{max(nums)} {min(nums)}"

print(high_and_low("1 9 3 4 -5"))