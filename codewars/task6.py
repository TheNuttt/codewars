# Задание 6: Расчет макс. скорости автомобиля по GPS-отметкам пути   

def gps(s, x):
    if len(x) <= 1:
        return 0
    speeds = [(x[i] - x[i - 1]) * 3600 / s for i in range(1, len(x))]
    return int(max(speeds))

print(gps(16, [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.32, 1.54]))