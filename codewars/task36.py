# Задача 36: Находит первый неповторяющийся символ в строке без учета регистра

def first_non_repeating_letter(s):
    lower_s = s.lower()
    for i, char in enumerate(lower_s):
        if lower_s.count(char) == 1:
            return s[i]
    return ""    

test_strings = ["stress", "sTreSS", "abba", "Go hang a salami, I'm a lasagna hog!"]

for text in test_strings:
    result = first_non_repeating_letter(text)
    print(f"Входная строка: '{text}' -> Первый уникальный символ: '{result}' ")