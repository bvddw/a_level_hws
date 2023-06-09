from Recruiter import Recruiter
from Developer import Developer
from func import compare, union_dev


developers = []
names_developers = []
recruiters = []
names_recruiters = []
while True:
    try:
        choice = int(input('Do you want to add a new employee?\n1. YES\n2. NO\n'))
        match choice:
            case 1:
                name = input('Enter employee name: ')
                while True:
                    try:
                        salary = float(input('Enter employee`s salary per day: '))
                        break
                    except ValueError:
                        print('You must enter float number for salary.')
                while True:
                    try:
                        oc_type = int(input("Enter occupation type\n1. Recruiter\n2. Developer\n"))
                        match oc_type:
                            case 1:
                                if name in names_recruiters:
                                    print('We already have this worker.')
                                    break
                                else:
                                    new_employee: Recruiter = Recruiter(name, salary)
                                    recruiters.append(new_employee)
                                    names_recruiters.append(name)
                                    break
                            case 2:
                                if name in names_developers:
                                    print('We already have this worker.')
                                    break
                                else:
                                    list_tech: list = input('Enter knowledge of this employee, separated by spaces: ').split()
                                    new_employee: Developer = Developer(name, salary, list_tech)
                                    developers.append(new_employee)
                                    names_developers.append(name)
                                    break
                            case _:
                                print('You need to enter 1 or 2.')
                    except ValueError:
                        print('You need to enter 1 or 2.')
            case 2:
                print('All employees added.')
                break
            case _:
                print('You need to enter 1 or 2.')
    except ValueError:
        print('Enter 1 or 2.')
print('\nList of recruiters:')
for i, human in enumerate(recruiters):
    print(f'ID: {i + 1}, {human}')
print('\nList of developers:')
for i, human in enumerate(developers):
    print(f'ID: {i + 1}, {human}')

if len(developers) + len(recruiters) > 1:
    while True:
        try:
            choice = int(input('Do you want to compare two employees?\n1. YES\n2. NO\n'))
            match choice:
                case 1:
                    print('\nList of recruiters:')
                    for i, human in enumerate(recruiters):
                        print(f'ID: {i + 1}, {human}')
                    print('\nList of developers:')
                    for i, human in enumerate(developers):
                        print(f'ID: {i + 1}, {human}')
                    print(compare())
                case 2:
                    break
                case _:
                    print('Enter 1 or 2.')
        except ValueError:
            print('Enter 1 or 2.')

if len(developers) > 1:
    cont: bool = True
    while cont:
        try:
            choice = int(input('Do you want union two Developers?\n1. YES\n2. NO\n'))
            match choice:
                case 1:
                    print(union_dev())
                case 2:
                    cont = False
                case _:
                    print('Incorrect choice.')
        except ValueError:
            print('Enter 1 or 2.')
print('\nList of recruiters:')
for i, human in enumerate(recruiters):
    print(f'ID: {i + 1}, {human}')
print('\nList of developers:')
for i, human in enumerate(developers):
    print(f'ID: {i + 1}, {human}')
print('Program finished successfully!')
