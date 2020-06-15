nomes = open("nbebes.txt", "r", errors='ignore')
#aqui coloquei os nomes em uma array por linha
n = nomes.readlines()
for nome in n[0]:
   print(nome)

nomes.close()