def digital_root(n):
    g = str(n); numbers = []
    for number in range(len(g)):
        numbers.append(int(g[number]))
    return digital_root(sum(numbers)) if len(numbers) > 1 else numbers[0]


