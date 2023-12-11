'''
    Acest modul contine o functie care poate detecta informatiile
    dintrun site si titlul ei
'''
import configparser # putem citi fileurile cu format .ini
import requests # conectarea cu pagina web
from bs4 import BeautifulSoup # manipularea datelor primite in format html, xml

def iniToDict(link: str) -> dict:
    '''
        Aceasta functie citeste un fisieri cu format .ini si il converteaza intrun dictionar
        iniToDict(link: str) -> dict unde linkul este locatia la fisier
    '''
    config = configparser.ConfigParser()
    
    config.read(link)
    
    d = {key:value for (key, value) in zip(config.sections(), [dict(config.items(config.sections()[i])) for i in range(len(config.sections()))])}
    
    return d

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
    config = iniToDict("config.ini")
    
    link = config["path"]["link"]

    info = getInfoLink(link)

    print('/////////////////////////////////////////')
    print("Titlul paginii: ", info['title'])
    print()
    print("Descrierea: ", info['description'])
    print('/////////////////////////////////////////')
    



