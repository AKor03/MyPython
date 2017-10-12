import math
print("a Ввел!")
a = float(input("a = "))
print("b Ввел!")
b = float(input("b = "))
print("c Ввел!")
c = float(input("c = "))
print("Красава!")

d = b ** 2 - 4 * a * c;
print("d = {}".format(d))
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = {}".format(x1))
    print("x2 = {}".format(x2))
elif d == 0:
    x = -b / (2 * a)
    print("Вот тебе корень x = {}".format(x))
else:
    print("Поц")
