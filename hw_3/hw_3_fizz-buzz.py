data = open('hw_3_fizz_buzz_input.txt', 'r')
f = open('hw_3_fizz_buzz_output.txt', 'w')
for line in data:
    numbers = line.split()
    fizz = int(numbers[0])
    buzz = int(numbers[1])
    number = int(numbers[2])
    answer = []
    for i in range(1, number + 1):
        if not i % fizz and i % buzz:
            answer.append('F')
        elif not i % buzz and i % fizz:
            answer.append('B')
        elif not i % fizz and not i % buzz:
            answer.append('FB')
        else:
            answer.append(str(i))
    f.write(' '.join(answer))
    f.write('\n')
f.close()