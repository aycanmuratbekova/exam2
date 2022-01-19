students = [
    {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Agness', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Don', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
    {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Alexey', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Mikel', 'age': 24, 'course': 'python', 'gender': 'Male'},
    {'name': 'Susanne', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Stevie', 'age': 26, 'course': 'python', 'gender': 'Male'},
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aktanbek', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
    {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
]

names = ['Janyl', 'Nursultan', 'Meerim', 'Emir', 'Susann', 'Marcus', 'Aidin',
         'Aigerim', 'Angela', 'Albert', 'Jyldyz', 'Doe', 'Gloria', 'Aliaskar',
         'Martin', 'John', 'Andrew', 'Steve', 'Johnathan', 'Adyl', 'Chyngyz',
         'Michael', 'Atay', 'Mikkel', 'Agnes', 'Aidana', 'Sultan', 'Nash',
         'Nicolas', 'Mirbek', 'Aktan', 'Emirlan', 'Jennifer', 'Eniston', 'Alex', 'Mark']



type_courses = ["python", "javascript", "java"]
names_py = []
names_js = []
names_jvm = []

#***********TASK-3-1*****************************************
def create_new_dic():
    for student in students:
        if student['course'] == 'python':
            names_py.append(student['name'])
        elif student['course'] == 'javascript':
            names_js.append(student['name'])
        elif student['course'] == 'java':
            names_jvm.append(student['name'])

    all_names = [names_py, names_js, names_jvm]
    new_dictionary = dict(zip(type_courses, all_names))
    return new_dictionary


student_names = []
student_ages = []

#***********TASK-3-2*****************************************
def name_age_dic():
    for student in students:
        student_names.append(student['name'])
        student_ages.append(student['age'])

    new_dictionary = dict(zip(student_names, student_ages))
    return new_dictionary




#***********TASK-3-3*****************************************
def try_find_age(names_, name_age):
    for i in names_:
        try:
            print(f'Имя {i}  : возраст {name_age[i]}')
        except:
            print(f'Имени {i} не существует в словаре')




print('\n***********TASK-3-1*****************************************')
print(create_new_dic())

print('\n***********TASK-3-2*****************************************')
print(name_age_dic())

print('\n***********TASK-3-3*****************************************')
try_find_age(names, name_age_dic())
