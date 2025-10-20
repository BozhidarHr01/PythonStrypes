def fib_range(start, end):
    saved = {}

    def fib(n):
        if n in saved:
            return saved[n]
        if n <= 1:
            result = n
        else:
            result = fib(n - 1) + fib(n - 2)
        
        saved[n] = result
        return result
    
    result = []
    for i in range(start - 1, end):
        result.append(str(fib(i)))
    
    return " ".join(result)

start, end = input().split()

print(fib_range(int(start), int(end)))