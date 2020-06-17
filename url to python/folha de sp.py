#this program only works with the brazilian journal Folha de São Paulo. I'll make some improvements. I'm still ex
#experimenting with selenium

from selenium import webdriver
import random

terms = input('qual o link da notícia?\n ')

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get(terms)

search = driver.find_element_by_class_name("c-news__body")

with open(str(random.randrange(0, 10000)) +'.doc', 'w') as o:
    o.write(search.text)


driver.quit()

