# Задача 26: определяет, является ли строка панграммой. Возвращает True, если является панграммой, False, если нет

def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    st_lower = st.lower()

    for char in alphabet:
        if char not in st_lower:
            return False
    return True    

print(is_pangram("The quick brown fox jumps over the lazy dog" ))    