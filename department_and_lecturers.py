from department_urls import parser

department_and_lecturers_dict = dict()


department_urls = [
    "https://acc.covenantuniversity.edu.ng/index.php/faculty/faculty",
    'https://arc.covenantuniversity.edu.ng/index.php/faculty',
    'https://bfn.covenantuniversity.edu.ng/index.php/faculty',
    'https://bld.covenantuniversity.edu.ng/index.php/faculty-management-team',
    'https://bch.covenantuniversity.edu.ng/index.php/staff/faculty',
    'https://bly.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://bus.covenantuniversity.edu.ng/index.php/faculty/facult',
    'https://che.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://chm.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://cis.covenantuniversity.edu.ng/index.php/faculty-management-team',
    'https://cve.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://eco.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://eie.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://esm.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://lge.covenantuniversity.edu.ng/index.php/faculty/',
    'https://mac.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://mat.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://mce.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://pet.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://phy.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://pol.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://psy.covenantuniversity.edu.ng/index.php/faculty/faculty',
    'https://soc.covenantuniversity.edu.ng/index.php/faculty/faculty'
]

def get_lecturers_names(list_of_spans):
    
    list_of_lecturers = list()
    
    for span in list_of_spans:
        list_of_lecturers.append(span.get_text())
    return list_of_lecturers



for url in department_urls:
    soup = parser(url)
    span_of_lecturers = soup.find_all('span', class_ = 'sppb-person-name')
    
    try:
        department_name = soup.find('img', class_="sp-default-logo")['alt']
    
    except TypeError:
        department_name = soup.find('img', class_="custom-logo")['alt']

    department_and_lecturers_dict[department_name] = get_lecturers_names(span_of_lecturers)


print('{')
for key, values in department_and_lecturers_dict.items():
    print(f'\'{key}\': [')
    for value in values:
        print(f'\t\'{value}\',')
    print(f'],')


