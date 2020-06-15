def to_jaden_case(string):
    count = 0
    for i in string:
        if string[count - 1] == " ":
            print(i.upper(), end = '')
        elif count == 0:
            print(i.upper(), end='')
        else:
            print(i, end = '')
        count += 1

print(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]))