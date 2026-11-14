# Задача 24: Возвращает первую самую длинную строку, состоящую из k последовательных строк, взятых из массива

def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    
    longest_str = ""
    for i in range(n - k + 1):
        current_str = "".join(strarr[i : i + k])
        if len(current_str) > len(longest_str):
            longest_str = current_str
            
    return longest_str   

print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2)) #пример из задачи