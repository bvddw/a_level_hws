data = open("hw_6_1_db.txt", 'r')
output = open("hw_6_1_output.txt", 'w')
people = {}
best = -1
worst = 101
best_student = ''
worst_student = ''
for line in data:
    name, marks = line.strip().split(':')
    people[name] = marks
    current = sum(list(map(int, marks.split()))) / 5
    if current > best:
        best = current
        best_student = name
    if current < worst:
        worst = current
        worst_student = name


output.write(f'The best student is {best_student} with average mark: {best}.\n')
output.write(f'The worst student is {worst_student} with average mark: {worst}.')
output.close()
