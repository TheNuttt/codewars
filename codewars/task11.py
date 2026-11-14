# Задача 11: Сортирует слова в строке на основе цифр, которая содержится внутри каждого слова

def order(sentence):
    if not sentence:
        return ""
    
    words = sentence.split()
    
    def get_number(word):
        for char in word:
            if char.isdigit():
                return int(char)
            
    sorted_words = sorted(words, key=get_number)
    return " ".join(sorted_words)

print(order("is2 Thi1s T4est 3f"))