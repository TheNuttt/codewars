# Задача 33: Принимает на вход строку и массив словарей и возвращает значения из словаря, начинающиеся с входной строки. Если совпадений больше 5, ограничивает вывод первыми 5 результатами

def autocomplete(input_, dictionary):
    clean_input = ""
    for char in input_:
        if char.isalpha():
            clean_input += char.lower()
            
    result = []        
    for word in dictionary:
        if word.lower().startswith(clean_input):
            result.append(word)
            if len(result) == 5:
                break
                
    return result            

words = ['airplane','airport','apple','ball']
print(autocomplete('ai', words))