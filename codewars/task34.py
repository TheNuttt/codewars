# Задача 34: Удаляет все круглые скобки вместе с их содержанием из строки

def remove_parentheses(st):
    result = []
    depth = 0
    
    for char in st:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        elif depth == 0:
            result.append(char)
        
    return ''.join(result)    

print(remove_parentheses("example(unwanted thing)example"))