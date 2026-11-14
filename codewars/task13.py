# Задача 13: Ребенок бросает мяч с высоты h. Мяч отскакиевает на высоту (h * bounce). Мама смотрит в окно на высоте window. Нужно посчитать  сколько раз мяч пролетит мимо окна

def bouncing_ball(h, bounce, window):
    if not(h > 0 and 0 < bounce < 1 and window < h):
        return -1
    
    seen = 0 
    while h > window:
        seen += 1
        h *= bounce
        if h > window:
            seen += 1
            
    return seen   

print(bouncing_ball(3, 1, 1.5))