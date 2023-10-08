import math

a, b, c = map(int, input("Enter the coefficients (a, b, c) for ax^2 + bx + c: ").split())

d = b ** 2 - 4 * a * c

if d == 0:
    x = -b / (2 * a)
    print("x =", x)
elif d > 0:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print("x =", x1, "or x =", x2)
else:
    print("No real solutions")
