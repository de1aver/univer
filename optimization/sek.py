def fx(x):
    return 3 * x ** 2 - (7/x)

def fx1(x):
    return 6 * x - (7/x ** 2)

def fx2(x):
    return 6 - (7/x ** 3)

def sek(iter):
    a = int(input("Левая граница интервала -  "))
    b = int(input("Правая граница интервала - "))
    x1 = float(input("Введите x1 - "))
    for i in range(iter):
        xn = b - fx(b) * ((x1 - b)/(fx(x1) - fx(b)))
        x1 = xn
        print(xn)

kolvo = int(input("Укажите количество итераций - "))
sek(kolvo)
#test end