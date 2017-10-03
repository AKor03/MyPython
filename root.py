import math
a = 2
b = 10
c = 4


d = ((b ** 2) - (4 * a * c))
#print(d)
#print((-b + math.sqrt(d)) / (2 * a))
x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)

print(x1)

print(x2)
print("x1 = {}".format(x1))
print("x2 = {}".format(x2))