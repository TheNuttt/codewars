# Задача 30: получает массив/список сигнатур , и возвращает первые n элементов (включая сигнатуру) из заданной последовательности

def tribonacci(signature, n):
    result = signature[:n]
    while len(result) < n:
        result.append(sum(result[-3:]))
        
    return result    

print(tribonacci([1,1,1], 8))