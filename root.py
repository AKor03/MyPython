import math
print("Введи значение a")
a = float(input("a = "))
print("Введи значение b")
b = float(input("b = "))
print("Введи значение c")
c = float(input("c = "))

d = b ** 2 - 4 * a * c;
print("d = {}".format(d))
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = {}".format(x1))
    print("x2 = {}".format(x2))
elif d == 0:
    x = -b / (2 * a)
    print("x = {}".format(x))
else:
    print("нет корня")
