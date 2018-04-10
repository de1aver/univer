def fx(x):
    return x*x*x + 8*x*x + x +5


def fx1(x):
    return 3*x*x + 16*x + 1

def cas(iter):
    x1 = float(input("Введите x1 - "))
    for i in range(iter):
        xn = x1 - (fx(x1)/fx1(x1))
        x1 = xn
        print("x = ", xn)

kolvo = int(input("Укажите количество итераций - "))
cas(kolvo)