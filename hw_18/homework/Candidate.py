import requests


class Candidate:
    def __init__(self, first_name: str, last_name: str, email: str, tech_stack: list, main_skill: str,
                 main_skill_grade: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    # add property self.fullname to Candidate
    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    # take data from url and save into candidates
    @classmethod
    def generate_candidates(cls, url: str):
        response = requests.get(url)
        data = response.text
        candidates: list = []
        for row in data.split('\n'):
            if row == '':
                continue
            info = row.split(',')
            if info[0] == 'Full Name':
                continue
            candidate: Candidate = Candidate(info[0].split()[0], info[0].split()[1], info[1], info[2].split('|'), info[3], info[4])
            candidates.append(candidate)
        return candidates
