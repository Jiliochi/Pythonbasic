#te da o valor
mounth_name = {"Jan" : "January", "Feb" : "Fevereiro"}
print(mounth_name["Jan"])
#pode ser get ou []. segundo argumento é o default
print(mounth_name.get("Dec", "not a valid key"))