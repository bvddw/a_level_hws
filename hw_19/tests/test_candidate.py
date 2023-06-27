from hw_19.classes.candidate.candidate import Candidate, GenerateCandidates, is_correct_email, is_correct_grade
import unittest
from unittest import mock
from unittest.mock import patch


class TestGenerateCandidates(unittest.TestCase):
    def test_generate_candidates_from_test_url(self):
        # Create an instance of GenerateCandidates
        generate_candidates = GenerateCandidates()

        # Mock the requests.get method to return test data
        mock_response = mock.Mock()
        mock_response.text = 'Full Name,Email,Technologies,Main Skill,Main Skill Grade\nJohn Doe,john.doe@example.com,Python|CSS,Python,Senior\n'
        with patch('requests.get', return_value=mock_response):
            # Call the generate_candidates_from_url method
            generate_candidates.generate_candidates_from_url('http://example.com')

        # Assert that the candidates were added to the list
        self.assertEqual(len(generate_candidates), 1)
        # Assert the properties of the added candidate
        candidate = generate_candidates[0]
        self.assertEqual(candidate.first_name, 'John')
        self.assertEqual(candidate.last_name, 'Doe')
        self.assertEqual(candidate.email, 'john.doe@example.com')
        self.assertEqual(candidate.tech_stack, ['Python', 'CSS'])
        self.assertEqual(candidate.main_skill, 'Python')
        self.assertEqual(candidate.main_skill_grade, 'Senior')

    def test_generate_candidates_from_url(self):
        # Create an instance of GenerateCandidates
        generate_candidates = GenerateCandidates()

        generate_candidates.generate_candidates_from_url('https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv')

        # Assert that the candidates were added to the list
        self.assertEqual(len(generate_candidates), 3)
        # Assert the properties of the added candidate
        candidate1 = generate_candidates[0]
        candidate2 = generate_candidates[1]
        candidate3 = generate_candidates[2]

        self.assertEqual(candidate1.first_name, 'Ivan')
        self.assertEqual(candidate1.last_name, 'Chechov')
        self.assertEqual(candidate2.email, 'mpayne@example.com')
        self.assertEqual(candidate2.tech_stack, ['PHP', 'Laravel', 'MySQL'])
        self.assertEqual(candidate3.main_skill, 'Python')
        self.assertEqual(candidate3.main_skill_grade, 'Junior')

    def test_is_correct_email(self):
        # Test a valid email
        valid_email = 'john.doe@example.com'
        self.assertTrue(is_correct_email(valid_email))

        # Test an invalid email
        invalid_email = 'john.doe'
        self.assertFalse(is_correct_email(invalid_email))

    def test_is_correct_grade(self):
        # Test a valid grade
        valid_grade = 'senior'
        self.assertTrue(is_correct_grade(valid_grade))

        # Test an invalid grade
        invalid_grade = 'manager'
        self.assertFalse(is_correct_grade(invalid_grade))

    def test_candidate_full_name(self):
        # Create a candidate instance
        candidate = Candidate('John', 'Doe', 'john.doe@example.com', [], '', '')

        # Assert the full_name property
        self.assertEqual(candidate.full_name, 'John Doe')
