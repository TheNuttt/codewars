# Задача 17: Возвращает количество шагов до первого совпадения значений на двух разнонаправленных кольцах

def spinning_rings(inner_max, outer_max):
    inner = 0
    outer = 0
    moves = 0
    
    while True:
        moves += 1
        inner = (inner - 1) % (inner_max + 1)
        outer = (outer + 1) % (outer_max + 1) 
        if inner == outer:
            return moves

print(spinning_rings(2, 3))            