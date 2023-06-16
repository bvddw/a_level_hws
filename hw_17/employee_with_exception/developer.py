from employee import Employee


# class Developer, have all attributes from Employee, and self.tech_stack (amount of knowledge)
class Developer(Employee):
    def __init__(self, name: str, salary: float, email: str, tech_list: list):
        super().__init__(name, salary, email)
        self.tech_stack: list = tech_list

    def __str__(self) -> str:
        return f"Developer: {self.name}, salary per day: {self.salary}, salary for this month: {self.month_salary()}, knowledge: {', '.join(self.tech_stack)}."

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def work(self) -> str:
        return 'I come to office and start to coding'

