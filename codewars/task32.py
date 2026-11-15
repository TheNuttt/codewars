# Задача 32: имея заданную строку, заменяет каждую букву на её позицию в алфавите

def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    position = []
    
    for char in text.lower():
        if char in alphabet:
            position.append(str(alphabet.index(char) + 1))
    
    return " ".join(position)

print(alphabet_position("The sunset sets at twelve o' clock."))