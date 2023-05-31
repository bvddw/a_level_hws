data = open('hw_9_third_input.txt', 'r')
output = open('hw_9_third_output.txt', 'w')
for line in data:
    sides = line.split(';')
    numbers = list(map(int, sides[0].split()))  # creating a list of numbers before ';'
    a = sum(numbers) // len(numbers)
    b = sum(numbers) % len(numbers)
    answer = list(map(int, sides[1].split()))  # creating a list of numbers after ';'
    func = answer[0] == a and answer[1] == b  # boolean result after checking
    output.write(line.strip() + ' ' + str(func) + '\n')
output.close()
