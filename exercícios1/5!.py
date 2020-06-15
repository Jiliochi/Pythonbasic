def iq_test(numbers):
    odd = []; even = []
    for m in numbers.split():
        odd.append(m) if int(m) % 2 != 0 else even.append(m)
    return numbers.split().index(even[0]) + 1 if len(odd) > 1 else numbers.split().index(odd[0])


print(iq_test("20 4 7 8 10"))

