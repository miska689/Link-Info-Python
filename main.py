import requests
from bs4 import BeautifulSoup

link = input("Introduceti linkul: ")

source = requests.get(link).text # primim raspunsul de la pagina

page = BeautifulSoup(source, 'html.parser')  

title_page = page.title.text # titlul paginii

description = page.find("meta", {"name":"description"}) # descrierea (daca nu exista are valuarea None)

print("Titul paginii: ", title_page)

print()

if description:
    print("Descrierea: ", description['content'])
else:
    print("Nu exista descriere la pagina!")
