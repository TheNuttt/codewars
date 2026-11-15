# Задача 35: Строит башню в виде пирамиды из символов "*" заданной высоты, возвращая ее в виде сптска строк с выравниваем по центру

def tower_builder(n_floors):
    tower = []
    width = 2 * n_floors - 1
    
    for i in range(1, n_floors + 1):
        stars = '*' * (2 * i - 1)
        tower.append(stars.center(width))
        
    return tower

for floor in tower_builder(3):
    print(f'"{floor}"')