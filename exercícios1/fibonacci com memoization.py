fibonacci_cache = {}

def fibonacci(n):
 if n in fibonacci_cache:
    return fibonacci_cache[n]

 if n == 1:
    value = 1
 elif n == 2:
    value = 2
 elif n > 2:
    value = fibonacci(n - 1) + fibonacci(n - 2)

 fibonacci_cache[n] = value
 return value

n = input("fibonacci series?\n")

for n in range(1, 1000):
 print(n,":", fibonacci(n),"\n")