# Задача 1

def count_by(x, n):
    return [i * x for i in range(1, n + 1)] 

print(count_by(1, 5))

# Задача 2

def greet(name):
    return f"Hello, {name} how are you doing today?"

print(greet("Ramina"))

# Задача 3

def repeat_str(repeat, string):
    return string * repeat

print(repeat_str(6, "I"))

# Задача 4

def litres(time):
    return int(time * 0.5)

print(litres(3))

# Задача 5

def invert(lst):
    return [ -x for x in lst]

print
# Задача 6

def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    
    if 90 <= score <=100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

# Задача 7

def make_upper_case(s):
    return s.upper()

#Задача 8

def find_smallest_int(arr): #нужно найти самое маленькое значение в списке
    return min(arr)     

# Задача 9

def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()

# Задача 10

def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"

#Задача 11

def row_sum_odd_numbers(n):
    return n ** 3



