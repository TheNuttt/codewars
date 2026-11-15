# Задача 23: Принимает строковый параметр и переворачивает каждое слово в строке

def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))

print(reverse_words("Мое величество устало"))   