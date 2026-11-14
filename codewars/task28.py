# Задание 28: Возвращает результат умножения этих чисел в порядке возрастания

def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result    

print(grow([1, 2, 5, 6]))