# Задача 15: Последовательно удаляет символы из строки по заданным индексам. после каждого удаления строка сжимается,пока не останется ровно один символ

def last_survivor(letters, coords): 
    letters_list = list(letters)
    for index in coords:
        letters_list.pop(index)
    return letters_list[0]

word = "pro"
positions = [0, 1]
result = last_survivor(word, positions)

print(f"Оставшийся символ: '{result}', индексы удаления: {positions}")