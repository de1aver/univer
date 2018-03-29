def fx(x):
    return 3 * x ** 2 - (7/x)

def fx1(x):
    return 6 * x - (7/x ** 2)

def cas(iter):
    x1 = float(input("Введите x1 - "))
    for i in range(iter):
        xn = x1 - (fx(x1)/fx1(x1))
        x1 = xn
        print("x = ", xn)

kolvo = int(input("Укажите количество итераций - "))
cas(kolvo)