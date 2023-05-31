database = open('hw_6_2_db.txt', 'r')
output = open('hw_6_2_output.txt', 'w')
two_more_groups = []
without_frontend = []
python_java = []
for line in database:
    name, list_of_groups = line.strip().split(':')
    groups = list_of_groups.split(', ')
    if len(groups) > 1:
        two_more_groups.append(name)
    if 'FrontEnd' not in groups:
        without_frontend.append(name)
    if 'Python' in groups or 'Java' in groups:
        python_java.append(name)
output.write(f"Students studying in two or more groups: {', '.join(two_more_groups)}.\n")
output.write(f"Students who are not studying on the frontend: {', '.join(without_frontend)}.\n")
output.write(f"Students learning Python or Java: {', '.join(python_java)}")
output.close()
