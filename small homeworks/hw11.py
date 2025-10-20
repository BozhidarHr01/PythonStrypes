def pow(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / pow(base, -power)
    else:
        return base * pow(base, power - 1)
    
n, power = input().split()

print(pow(int(n), int(power)))