import requests

FIRST_NAME = 0
SECOND_NAME = 1
FULL_NAME = 0
EMAIL = 1
TECH = 2
MAIN_SKILL = 3
MAIN_SKILL_GRADE = 4
GRADE = ['senior', 'middle', 'junior', 'trainee']


def is_correct_email(e_mail: str) -> bool:
    return '@' in e_mail


def is_correct_grade(grade: str) -> bool:
    return grade in GRADE


class GenerateCandidates(list):
    def generate_new_candidate(self):
        first_name = input('Enter candidate`s first name: ')
        second_name = input('Enter candidate`s second name: ')
        email = input('Enter candidate`s E-mail: ')
        while not is_correct_email(email):
            email = input('Invalid E-mail.\nEnter candidate`s E-mail: ')
        tech_skill = list(input('Enter the technologies that the candidate owns (separated by space): ').split())
        main_skill = input('Enter candidate`s main skill: ')
        grade = input('Enter grade of main skill: ')
        while not is_correct_grade(grade.lower()):
            grade = input('Invalid grade.\nEnter grade of main skill: ')
        new_candidate: Candidate = Candidate(first_name.lower().capitalize(), second_name.lower().capitalize(), email, tech_skill, main_skill, grade.lower().capitalize())
        self.append(new_candidate)

    def generate_candidates_from_url(self, url: str):
        response = requests.get(url)
        data = response.text
        for row in data.split('\n'):
            if row == '':
                continue
            info = row.split(',')
            if info[FULL_NAME] == 'Full Name':
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
            candidate: Candidate = Candidate(info[FULL_NAME].split()[FIRST_NAME], info[FULL_NAME].split()[SECOND_NAME],
                                             info[EMAIL], info[TECH].split('|'), info[MAIN_SKILL],
                                             info[MAIN_SKILL_GRADE])
            self.append(candidate)


class Candidate:
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

    def __str__(self) -> str:
        return f'FullName: {self.full_name}, Email: {self.email}, Technologies: {self.tech_stack}, Main skill: {self.main_skill}, Main skill grade: {self.main_skill_grade}.'

    # add property self.fullname to Candidate
    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @staticmethod
    def list_of_candidates():
        candidate_list = GenerateCandidates()
        while True:
            try:
                choice = int(input('Do you want to add a new candidate? (1 - yes, 2 - no): '))
                match choice:
                    case 1:
                        candidate_list.generate_new_candidate()
                    case 2:
                        break
                    case _:
                        print('Invalid choice.')
            except ValueError:
                print('Choice number, please.')

        candidate_list.generate_candidates_from_url(
            'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv')
        return candidate_list
