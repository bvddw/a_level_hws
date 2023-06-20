from hw_19.classes.developer import Developer
from unittest import TestCase


class TestDeveloper(TestCase):
    def setUp(self) -> None:
        self.developer_1 = Developer('Benjamin', 220, 'ben@gmail.com', ['Python', 'C++'])
        self.developer_2 = Developer('Sophia', 210, 'ben@gmail.com', ['Python', 'JS', 'MySQL'])

    def test_tech(self):
        self.assertTrue(self.developer_1 < self.developer_2)

    def test_work(self):
        self.assertEqual('I come to office and start to coding.', self.developer_1.work())
        self.assertEqual('I come to office and start to coding.', self.developer_2.work())