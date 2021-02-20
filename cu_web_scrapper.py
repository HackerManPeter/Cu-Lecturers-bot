import requests
import re
from bs4 import BeautifulSoup as bs





cu_url = 'https://covenantuniversity.edu.ng'
def parser(url):
    '''
    Parse url into Beautiful soups
    '''
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    return soup
    
#Use requests to get page contents and send to BS
url = 'https://covenantuniversity.edu.ng/Colleges'
soup = parser(url)



staff_pages = [
    'https://covenantuniversity.edu.ng/Colleges/COE/SOCPE/Chemical-Engineering#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/COE/SOCPE/Petroleum-Engineering#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/COE/SOCPE/Electrical-Information-Engineering-EIE#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/COE/SOCPE/Civil-Engineering#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/COE/SOCPE/Mechanical-Engineering#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CLDS/SLD/Leadership-Studies#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CLDS/SLD/Languages-and-General-Studies#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CLDS/SLD/Psychology#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CLDS/SLD/Political-Science-International-Relations#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CMSS/SOB/Accounting#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CMSS/SOB/Banking-And-Finance#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CMSS/SOB/Business-Management#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CMSS/SOB/Economics-and-Development-Studies#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CMSS/SOB/Mass-Communication#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CMSS/SOB/Sociology#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CST/SNAS/Physics#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CST/SNAS/Building-Technology#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CST/SNAS/Chemistry#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CST/SNAS/Mathematics#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CST/SNAS/Biochemistry#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CST/SNAS/Computer-Information-Sciences#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CST/SNAS/Architecture#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CST/SNAS/Estate-Management#tab_staff_personnel',
    'https://covenantuniversity.edu.ng/Colleges/CST/SNAS/Biological-Sciences#tab_staff_personnel'
    ]

department_database = dict()


# Creates a dictionary where each department is a key and the  value is a list of lecturers
for num in range(len(staff_pages)):
    staff_links = list()
    page_soup = parser(staff_pages[num])
    staff_names = page_soup.body.find_all('h3', class_='bold arial size16 office-view-name')
    for item in staff_names:
        staff_links.append(item.find('a', href = re.compile('Profiles')))
    department_name = re.search('.+/Colleges/([A-Z]{3,4}).+/(\w.+)#', str(staff_pages[num])).group(2)
    #college_name = re.search('.+/Colleges/([A-Z]{3,4}).+/(\w.+)#', str(staff_pages[num])).group(1)
    if None in staff_links:staff_links.remove(None)
    department_database[department_name] = staff_links

# main program


def call_lecturer(user_input):
    '''
    passes a string into the dictionary and returns messages containing lecturrs name, department 
    and link to Covenant University profile
    '''
    delete = ['dr.','dr', 'mr.', 'mr', 'mrs.', 'mrs', 'engr.', 'engr', 'prof.', 'prof']
    user_input = user_input.split()
    [user_input.remove(item) for item in user_input if item.lower() in delete]
    lecturer_info= list()
    count = 0
    regex = re.compile('href="(/.+)"')
    for name_of_lecturer in user_input:
        for key, value in department_database.items():
            for name in value:
                if name_of_lecturer.lower() in str(name).lower(): 
                    lecturer_name = name.text.strip()
                    lecturer_link = cu_url + regex.search(str(name)).group(1)
                    lecturer_department = key
                    message = '\n\n\nWe found: \n' + lecturer_name + '\n\nFrom the department of\n' + lecturer_department +'\n\nFor more information visit: \n' + lecturer_link
                    lecturer_info.append(message)
                    count = count + 1
        if count == 0:
            message = 'No Lecturer was found'
            lecturer_info.append(message)
    
    lecturer_info = list(set(lecturer_info))
        
    return lecturer_info

