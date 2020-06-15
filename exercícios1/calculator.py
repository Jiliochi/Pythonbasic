from math import *

x = input("Which arimetic function you wish to calculate? (sq, +, -, *, /, power)\n")

if x == "sq":
    y = 1
elif x == "power":
    y = 2
else:
    y = int(input("how many digits?\n"))
    if y > 2:
        print("ERROR 101")
        exit(1)

letters = ["e", "h"]
for number in range(y):
    if number == 1:
        letters[0] = int((input("first number: ")))
    if number == 2:
        letters[1] =int((input("second number: ")))

if x == "+":
    print(int(letters[0]) + int(letters[1]))
elif x == "-":
    print(int(letters[0]) - int(letters[1]))
elif x == "*":
    print(int(letters[0]) * int(letters[1]))
elif x == "/":
    print(int(letters[0]) / int(letters[1]))
elif x == "sq":
    print(sqrt(int(letters[0])))
elif x == "power":
    print(pow(int(letters[0]), int(letters[1])))
else:
    print("ERROR")





