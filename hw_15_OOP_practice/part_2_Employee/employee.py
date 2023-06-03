class Employee:
    def __init__(self, _name: str, _salary: float) -> None:
        self.name = _name
        self.salary = _salary

    def __str__(self) -> str:
        return f'Name - {self.name}, salary - {self.salary}'

    def work(self) -> str:
        return f"{self.name} comes to the office."

    def __gt__(self, other) -> bool:
        return self.salary > other.salary

    def __lt__(self, other) -> bool:
        return self.salary < other.salary

    def __ge__(self, other) -> bool:
        return self.salary >= other.salary

    def __le__(self, other) -> bool:
        return self.salary <= other.salary


class Recruiter(Employee):
    def __init__(self, _name: str, _salary: float):
        super().__init__(name, salary)

    def work(self) -> str:
        return 'I come to office and start to hiring'

    def __str__(self) -> str:
        return f'Recruiter: {self.name}.'


class Developer(Employee):
    def __init__(self, _name: str, _salary: float):
        super().__init__(name, salary)

    def work(self) -> str:
        return 'I come to office and start to coding'

    def __str__(self) -> str:
        return f'Developer: {self.name}.'


def compare() -> str:
    name_1: str = input('Enter first employee name: ')
    while True:
        try:
            oc_type_1: int = int(input("Enter occupation type (1 - Recruiter, 2 - Developer): "))
            if oc_type_1 == 1:
                if name_1 in names_recruiters:
                    worker_1: Recruiter = recruiters[names_recruiters.index(name_1)]
                    break
                else:
                    print('We do not have this employeer.')
                    break
            elif oc_type_1 == 2:
                if name_1 in names_developers:
                    worker_1: Developer = developers[names_developers.index(name_1)]
                    break
                else:
                    print('We do not have this employeer.')
                    break
            else:
                print('You need to enter 1 or 2.')
        except ValueError:
            print('You need to enter 1 or 2.')

    name_2: str = input('Enter first employee name: ')
    while True:
        try:
            oc_type_2: int = int(input("Enter occupation type (1 - Recruiter, 2 - Developer): "))
            if oc_type_2 == 1:
                if name_2 in names_recruiters:
                    worker_2: Recruiter = recruiters[names_recruiters.index(name_2)]
                    break
                else:
                    print('We do not have this employeer.')
            elif oc_type_2 == 2:
                if name_2 in names_developers:
                    worker_2: Developer = developers[names_developers.index(name_2)]
                    break
                else:
                    print('We do not have this employeer.')
            else:
                print('You need to enter 1 or 2.')
        except ValueError:
            print('You need to enter 1 or 2.')
    return f'Is worker 1 have bigger salary than worker 2: {worker_1 > worker_2}'


developers = []
names_developers = []
recruiters = []
names_recruiters = []
while True:
    choice = input('Do you want to add a new employee? (yes (in any register) if want, any other input if do not want) ')
    if choice.lower() == 'yes':
        name = input('Enter employee name: ')
        while True:
            try:
                salary = float(input('Enter employee`s salary per day: '))
                break
            except ValueError:
                print('You must enter float number for salary.')
        while True:
            try:
                oc_type = int(input("Enter occupation type (1 - Recruiter, 2 - Developer): "))
                if oc_type == 1:
                    if name in names_recruiters:
                        print('We already have this worker.')
                        break
                    else:
                        new_employee: Recruiter = Recruiter(name, salary)
                        recruiters.append(new_employee)
                        names_recruiters.append(name)
                        break
                elif oc_type == 2:
                    if name in names_developers:
                        print('We already have this worker.')
                        break
                    else:
                        new_employee: Developer = Developer(name, salary)
                        developers.append(new_employee)
                        names_developers.append(name)
                        break
                else:
                    print('You need to enter 1 or 2.')
            except ValueError:
                print('You need to enter 1 or 2.')
    else:
        print('All employees added.')
        break
print('\nList of recruiters:')
for i, human in enumerate(recruiters):
    print(f'ID: {i + 1}, {human}')
print('\nList of developers:')
for i, human in enumerate(developers):
    print(f'ID: {i + 1}, {human}')

if len(developers) + len(recruiters) > 1:
    while True:
        choice = input('Do you want to compare two employees? (yes (in any register) if want, any other input if do not want) ')
        if choice.lower() == 'yes':
            print(compare())
        else:
            print('Program completed.')
            break
