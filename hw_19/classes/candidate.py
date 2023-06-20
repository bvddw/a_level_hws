import requests


class Candidate:
    # some constance for better view of code
    FIRST_NAME = 0
    SECOND_NAME = 1
    FULL_NAME = 0
    EMAIL = 1
    TECH = 2
    MAIN_SKILL = 3
    MAIN_SKILL_GRADE = 4

    def __init__(self, first_name: str,
                 last_name: str,
                 email: str,
                 tech_stack: list,
                 main_skill: str,
                 main_skill_grade: str
                 ) -> None:
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
            if info[cls.FULL_NAME] == 'Full Name':
                continue
            """
            info[cls.FULL_NAME].split()[cls.FIRST_NAME] - (string) - first name
            info[cls.FULL_NAME].split()[cls.SECOND_NAME] - (string) - second name
            info[cls.EMAIL] - (string) - email
            info[cls.TECH].split('|') - (list) - tech_stack, but when we will write it in .csv file
                                                        we will use .join(), so it will be a string
            info[cls.MAIN_SKILL] - (string) - main skill
            info[cls.MAIN_SKILL_GRADE] - (string) - main skill grade
            """
            candidate: Candidate = Candidate(info[cls.FULL_NAME].split()[cls.FIRST_NAME], info[cls.FULL_NAME].split()[cls.SECOND_NAME], info[cls.EMAIL], info[cls.TECH].split('|'), info[cls.MAIN_SKILL], info[cls.MAIN_SKILL_GRADE])
            candidates.append(candidate)
        return candidates