a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a == 0:
    if b == 0:
        print("special case")
    else:
        x = -c / b
        print(x)
else:
    D = b * b - 4 * a * c
    if D < 0:
        print("no real roots")
    elif D == 0:
        x = -b / (2 * a)
        print(x)
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print(f"{x1}|{x2}")
