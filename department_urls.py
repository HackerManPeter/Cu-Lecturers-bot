import requests
from bs4 import BeautifulSoup as bs



cu_url = 'https://covenantuniversity.edu.ng'
department_information_url = 'https://covenantuniversity.edu.ng/information/information-for/departments'

def parser(url):
    '''
    Parse url into Beautiful soups
    '''
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    return soup

def get_department_url(deparment_anchors):
    '''
    Returns a list of urls from a list of anchor tags
    '''
    department_urls = list()

    for anchor in department_anchors:
        soup = bs(repr(anchor), 'html.parser')
        department_urls.append(soup.a['href'])

    
    return list(set(department_urls))

def get_department_names(department_anchors):

    department_names = dict()
    for anchor in department_anchors:
        soup = parser(anchor, 'html.parser')
        


soup = parser(department_information_url)

department_anchors = soup.find_all('a', class_ = 'last-child')
department_names = soup.find_all('a', class_='last-child')

department_names = list(set(department_names))

department_urls = get_department_url(department_anchors)


