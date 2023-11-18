'''
    Acest modul contine o functie care poate detecta informatiile
    dintrun site si titlul ei
'''

import requests # conectarea cu pagina web
from bs4 import BeautifulSoup # manipularea datelor primite in format html, xml

def getInfoLink(link: str) -> dict:
    '''
        Aceasta functie face parsing la o pagina si 
        colecteaza titlul paginii si descrierea 
        din tag-ul <meta>
        
        Ca parametrii avem linkul - tip string
        Ca date de esire avem un dictionar - tip dict
        
        {
            "title": "titlul_paginii"
            "description": "descrierea paginii"
        }
    '''
    source = requests.get(link).text # primim raspunsul de la pagina

    page = BeautifulSoup(source, 'html.parser')  

    title_page = page.title.text # titlul paginii

    description = page.find("meta", {"name":"description"}) # descrierea (daca nu exista are valuarea None)
    
    if description: 
        description = description['content']
    else:
        description = "Nu exista"
    
    return {'title': title_page, 'description': description}


if __name__ == "__main__":
    link = input("Introduceti linkul:")

    info = getInfoLink(link)

    print('/////////////////////////////////////////')
    print("Titlul paginii: ", info['title'])
    print()
    print("Descrierea: ", info['description'])
    print('/////////////////////////////////////////')




