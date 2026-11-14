# Задача 12: Находит и возвращает слово с наибольшим количеством очков

def high(x):
    words = x.split()
    highest_word = ""
    highest_score = 0
    
    for word in words:
        score = sum(ord(char) - 96 for char in word)
        if score > highest_score:
            highest_score = score
            highest_word = word
            
    return highest_word   

print(high("i need a car for my trip"))