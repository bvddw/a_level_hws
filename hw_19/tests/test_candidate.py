from hw_19.classes.candidate import Candidate
from unittest import TestCase


class TestCandidate(TestCase):
    def setUp(self) -> None:
        self.candidate = Candidate('Bob', 'Smith', 'bob@gmail.com', ['Python', 'C++'], 'Python', 'Middle')

    def test_equal(self):
        self.assertEqual('Bob Smith', self.candidate.full_name)

    def test_main_skill(self):
        self.assertIn(self.candidate.main_skill, self.candidate.tech_stack)

