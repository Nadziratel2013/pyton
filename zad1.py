import math

def decorator(resh):
    def wrapper(v0,v1,t):
        a=resh(v0,v1,t)
        x=v1*t+(a*(t**2))/2
        print("Находим укорение:")
        print(a)
        print("Находим расстояние:")
        print(x)


    return wrapper

@decorator
def resh(v0,v1,t):
    a=(v1-v0)/t

    return a

try:
    v0= float(input("Введите начальную скороть: "))
    v1 = float(input("Введите конечную скороть: "))
    t = float(input("Введите время: "))
    a=resh(v0,v1,t)
except ValueError:
    print("Нельзя вводить строки")
except ZeroDivisionError:
    print("Нельзя делить на ноль")


