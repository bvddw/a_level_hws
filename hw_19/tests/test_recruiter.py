from hw_19.classes.recruiter import Recruiter
from unittest import TestCase


class TestRecruiter(TestCase):
    def setUp(self) -> None:
        self.recruiter_1 = Recruiter('Emily', 210, 'emily@gmail.com')
        self.recruiter_2 = Recruiter('William', 220, 'wil@gmail.com')

    def test_salary_check(self):
        self.assertTrue(self.recruiter_2 > self.recruiter_1)

    def test_worl(self):
        self.assertEqual('I come to office and start to hiring.', self.recruiter_1.work())
        self.assertEqual('I come to office and start to hiring.', self.recruiter_2.work())