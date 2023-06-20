from hw_19.classes.employee import Employee
from unittest import TestCase


class TestEmployee(TestCase):
    def setUp(self) -> None:
        self.employee_1 = Employee('Jack', 200, 'jack@gmail.com')
        self.employee_2 = Employee('Bob', 210, 'bob@gmail.com')

    def test_str(self):
        self.assertEqual('Name - Jack, salary - 200', str(self.employee_1))
        self.assertEqual('Name - Bob, salary - 210', str(self.employee_2))

    def test_salary(self):
        self.assertTrue(self.employee_1 < self.employee_2)
