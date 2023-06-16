import csv
from candidate import Candidate


class CSV:
    FILENAME = 'data.csv'

    # method for save header for each column
    def save_header(self):
        with open(self.FILENAME, 'w', newline='') as file:
            csv.writer(file).writerow(['Full Name', 'Email', 'Technologies', 'Main Skill', 'Main Skill Grade'])

    # method for save data about chosen person
    def save_data(self, full_name: str, email: str, tech: list, main_skill: str, main_skill_grade: str) -> None:
        with open(self.FILENAME, 'a', newline='') as file:
            csv.writer(file).writerow([full_name, email, ' '.join(tech), main_skill, main_skill_grade])


save_data: CSV = CSV()
save_data.save_header()
# request data from link in arg
candidates = Candidate.generate_candidates(
    "https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv")
# save into data.csv file
for candidate in candidates:
    save_data.save_data(candidate.full_name, candidate.email, candidate.tech_stack, candidate.main_skill, candidate.main_skill_grade)