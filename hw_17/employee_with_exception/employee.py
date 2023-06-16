import csv
from datetime import datetime
from exceptions import EmailAlreadyExistsException


# check if .csv already has some info
def is_empty():
    with open('info.csv', 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            if row[1] == 'Email':
                return False
    return True


# if .csv file is empty - print there 'Name' and 'Info' - two columns
with open('info.csv', 'a', newline='') as file:
    if is_empty():
        csv.writer(file).writerow(['Name', 'Email'])


# email availability check functon
def email_exists(email):
    with open('info.csv', 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            if row[1] == email:
                return True
    return False


# class Employee, attributes: name, salary, email
class Employee:
    def __init__(self, name: str, salary: float, email: str) -> None:
        if email_exists(email):
            raise EmailAlreadyExistsException('Email already exist.')
        else:
            self.name = name
            self.salary = salary
            self.email = email
            self.save_email()

    def __str__(self) -> str:
        return f'Name - {self.name}, salary - {self.salary}'

    def __gt__(self, other) -> bool:
        return self.salary > other.salary

    def __lt__(self, other) -> bool:
        return self.salary < other.salary

    def work(self) -> str:
        return f"{self.name} comes to the office."

    # function for write info about employee in .csv file
    def save_email(self):
        with open('info.csv', 'a', newline='') as file:
            csv.writer(file).writerow([self.name, self.email])

    # a function to check the salary for this month (from its beginning to today)
    def month_salary(self) -> float:
        day = datetime.now().day
        week_day = datetime.now().weekday()
        work_days = 0
        for i in range(day, 0, -1):
            if 0 <= week_day <= 4:
                work_days += 1
            week_day -= 1 if week_day else -6
        return work_days * self.salary