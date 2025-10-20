def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    return base * power(base, exponent - 1)

print(power(int(input()), int(input())))