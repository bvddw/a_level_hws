from datetime import datetime


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def __str__(self) -> str:
        return f'Name - {self.name}, salary - {self.salary}'

    def __gt__(self, other) -> bool:
        return self.salary > other.salary

    def __lt__(self, other) -> bool:
        return self.salary < other.salary

    def work(self) -> str:
        return f"{self.name} comes to the office."

    def month_salary(self) -> float:
        day = datetime.now().day
        week_day = datetime.now().weekday()
        work_days = 0
        for i in range(day, 0, -1):
            if 0 <= week_day <= 4:
                work_days += 1
            week_day -= 1 if week_day else -6
        return work_days * self.salary
