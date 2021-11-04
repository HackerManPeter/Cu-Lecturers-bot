from department_and_lecturers import department_and_lecturers_dict

user_input = 'azu'

for department_name, lecturers in department_and_lecturers_dict.items():
    for lecturer in lecturers:
        if user_input in lecturer.lower():
            print(lecturer)
            print(department_name)
            print()
        
    
