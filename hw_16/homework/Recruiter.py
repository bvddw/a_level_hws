from Employee import Employee


class Recruiter(Employee):
    def __str__(self) -> str:
        return f"Developer: {self.name}, salary per day: {self.salary}, salary for this month: {self.month_salary()}."

    def work(self) -> str:
        return 'I come to office and start to hiring'
