def to_jaden_case(string):
    count = 0; ls = []
    for i in string:
        ls.append(i.upper()) if string[count - 1] == " " or count == 0 else ls.append(i)
        count += 1
    return "".join(ls)

print(to_jaden_case("most recent call last"))


