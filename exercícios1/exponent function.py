def power(num1, num2):
    result = 1
    for index in range(num2):
        result *= num1
    return result

g = power(2, 0)
print(g)