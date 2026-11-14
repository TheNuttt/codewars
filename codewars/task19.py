# Задача 19: Находит и возвращает число, которое встречается в списке нчетное кол-во раз 

def find_it(seq):
    result = 0
    for num in seq:
        result ^= num
    return result

print(find_it([1,1,2,4,4,5,3,5,2]))