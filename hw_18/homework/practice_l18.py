import csv
from Candidate import Candidate


# request data from link in arg
candidates_ = Candidate.generate_candidates("https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv")
# save into data.csv file
with open('data.csv', 'a', newline='') as file:
    csv.writer(file).writerow(['Full Name', 'Email', 'Technologies', 'Main Skill', 'Main Skill Grade'])
    for candidate in candidates_:
        csv.writer(file).writerow([candidate.full_name, candidate.email, ' '.join(candidate.tech_stack), candidate.main_skill, candidate.main_skill_grade])
