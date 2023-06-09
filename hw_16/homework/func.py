from Recruiter import Recruiter
from Developer import Developer


def compare(names_recruiters, names_developers, recruiters, developers) -> str:
    count_dev = 0
    is_first_dev: bool = False
    while True:
        try:
            oc_type_1: int = int(input("Enter first employee occupation type\n1. Recruiter\n2. Developer\n"))
            try:
                id_1: int = int(input('Enter first employee ID: '))
                match oc_type_1:
                    case 1:
                        if id_1 - 1 in range(len(names_recruiters)):
                            worker_1: Recruiter = recruiters[id_1 - 1]
                            print('Employer found.')
                            break
                        else:
                            print('We do not have employee with such ID.')
                    case 2:
                        if id_1 - 1 in range(len(names_developers)):
                            worker_1: Developer = developers[id_1 - 1]
                            count_dev += 1
                            is_first_dev = True
                            print('Employer found.')
                            break
                        else:
                            print('We do not have employee with such ID.')
                    case _:
                        print('You need to enter 1 or 2.')
            except ValueError:
                print('You need to enter the integer number.')
        except ValueError:
            print('You need to enter 1 or 2.')

    while True:
        try:
            oc_type_2: int = int(input("Enter second workers occupation type\n1. Recruiter\n2. Developer\n"))
            match oc_type_2:
                case 1:
                    try:
                        id_2: int = int(input('Enter second employee ID: '))
                        if id_2 - 1 in range(len(names_recruiters)):
                            worker_2: Recruiter = recruiters[id_2 - 1]
                            print('Employer found.')
                            break
                        else:
                            print('We do not have employee with such ID.')
                    except ValueError:
                        print('You need to enter the integer number.')
                case 2:
                    try:
                        id_2: int = int(input('Enter second employee ID: '))
                        if id_2 - 1 in range(len(names_developers)):
                            worker_2: Developer = developers[id_2 - 1]
                            count_dev += 1
                            print('Employer found.')
                            break
                        else:
                            print('We do not have employee with such ID.')
                    except ValueError:
                        print('You need to enter the integer number.')
                case _:
                    print('You need to enter 1 or 2.')
        except ValueError:
            print('You need to enter 1 or 2.')
    if count_dev == 2:
        if worker_1 > worker_2:
            return f'{worker_1.name} knows more than {worker_2.name}.'
        elif worker_2 > worker_1:
            return f'{worker_2.name} knows more than {worker_1.name}.'
        else:
            return f'{worker_1.name} knows same amount of tech with {worker_2.name}.'
    if count_dev == 1 and is_first_dev:
        if worker_2 > worker_1:
            return f'{worker_2.name} has bigger salary than {worker_1.name}'
        elif worker_2 < worker_1:
            return f'{worker_1.name} has bigger salary than {worker_2.name}'
        else:
            return f'{worker_2.name} has the same salary with {worker_1.name}'
    if worker_1 > worker_2:
        return f'{worker_1.name} has bigger salary than {worker_2.name}'
    elif worker_1 < worker_2:
        return f'{worker_2.name} has bigger salary than {worker_1.name}'
    else:
        return f'{worker_1.name} has the same salary with {worker_2.name}'


def union_dev(names_developers, developers) -> Developer:
    print('\nList of developers:')
    for i, human in enumerate(developers):
        print(f'ID: {i + 1}, {human}')
    while True:
        try:
            id_1: int = int(input('Enter first worker id: '))
            if id_1 - 1 in range(len(names_developers)):
                print('Worker found.')
                break
            else:
                print('Worker not found.')
        except ValueError:
            print('You need to enter the integer number.')
    while True:
        try:
            id_2: int = int(input('Enter second worker id: '))
            if id_2 == id_1:
                print('You already picked this employee.')
                continue
            if id_2 - 1 in range(len(names_developers)):
                print('Worker found.')
                break
            else:
                print('Worker not found.')
        except ValueError:
            print('You need to enter the integer number.')
    dev1 = developers[id_1 - 1]
    dev2 = developers[id_2 - 1]
    name_dev: str = dev1.name + ' ' + dev2.name
    list_tech_dev: list = list(set(dev1.tech_stack).union(set(dev2.tech_stack)))
    salary_dev: float = dev1.salary if dev1.salary > dev2.salary else dev2.salary
    dev: Developer = Developer(name_dev, salary_dev, list_tech_dev)
    developers.append(dev)
    names_developers.append(dev.name)
    return dev
