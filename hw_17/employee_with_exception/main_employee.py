# imports
from Recruiter import Recruiter
from Developer import Developer
from func import compare, union_dev
from exceptions import EmailAlreadyExistsException
import csv
from datetime import datetime
import traceback


# checking if email already exist in .csv file
def email_exists(email):
    with open('info.csv', 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            if row[1] == email:
                return True
    return False


# function for write exception in logs.txt
def log_exception():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    traceback_info = traceback.format_exc()

    log_message = f"{timestamp} | {traceback_info}"

    with open('logs.txt', 'a') as log_file:
        log_file.write(log_message + '\n')


# main part
developers = []
names_developers = []
recruiters = []
names_recruiters = []
# adding new employee
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
                    email = input('Enter employee email: ')
                    if '@' not in email:
                        print('There no "@" in your email.')
                    else:
                        break
                while True:
                    try:
                        oc_type = int(input("Enter occupation type\n1. Recruiter\n2. Developer\n"))
                        match oc_type:
                            case 1:
                                try:
                                    new_employee: Recruiter = Recruiter(name, salary, email)
                                    recruiters.append(new_employee)
                                    names_recruiters.append(name)
                                except EmailAlreadyExistsException:
                                    log_exception()
                                break
                            case 2:
                                list_tech: list = input('Enter knowledge of this employee, separated by spaces: ').split()
                                new_employee: Developer = Developer(name, salary, email, list_tech)
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
# output info for user
print('\nList of recruiters:')
for i, human in enumerate(recruiters):
    print(f'ID: {i + 1}, {human}')
print('\nList of developers:')
for i, human in enumerate(developers):
    print(f'ID: {i + 1}, {human}')

# if user want to compare two employees
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
                    print(compare(names_recruiters, names_developers, recruiters, developers))
                case 2:
                    break
                case _:
                    print('Enter 1 or 2.')
        except ValueError:
            print('Enter 1 or 2.')

# if user want to union two developers
if len(developers) > 1:
    cont: bool = True
    while cont:
        try:
            choice = int(input('Do you want union two Developers?\n1. YES\n2. NO\n'))
            match choice:
                case 1:
                    print(union_dev(names_developers, developers))
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
