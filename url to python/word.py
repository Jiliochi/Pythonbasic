from bs4 import BeautifulSoup
import urllib.request


#abrir onde vai escrever
file = open(<document name>, "w", errors='ignore')

#abrir onde vai ler
weburl = urllib.request.urlopen(<site>)

#ler do html
soup = BeautifulSoup(weburl.read(), "html.parser")

#escrever
file.write(soup.get_text('\n'))

file.close()