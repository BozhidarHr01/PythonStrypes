def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fibbonaci_numbers = [0, 1]

    for i in range(2, n):
        next_fib = fibbonaci_numbers[i - 1] + fibbonaci_numbers[i - 2]
        fibbonaci_numbers.append(next_fib)
    
    return fibbonaci_numbers

# 0 1 2 3 4 5 6 7  8
# 0 1 1 2 3 5 8 13 21
#recursive:
def fibonacci_recursive(n):
    stored_values = {0 : 0, 1 : 1}

    def fib(x):
        if x in stored_values:
            return stored_values[x]
        
        result = fib(x - 1) + fib(x - 2)

        stored_values[x] = result
        return result

    sequence = []
    for i in range(n):
        sequence.append(fib(i))
    
    return sequence
#tests
# print(fibonacci(int(input())))
print(fibonacci_recursive(int(input())))