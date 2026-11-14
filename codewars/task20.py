# Задача 20: Принимает положительный параметр num и возвращает его мультипликативную постоянную, то есть количество раз, которое необходимо умножить цифры в , numчтобы получить однозначное число.

def persistence(n):
    count = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        count += 1
    return count 

print(persistence(334))