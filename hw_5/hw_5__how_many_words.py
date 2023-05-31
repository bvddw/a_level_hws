data = open('hw_5_input.txt', 'r')
f = open('hw_5_output.txt', 'w')
dif_words = {}
for line in data:
    line = line.rstrip()  # прибираємо символ переходу на новий рядок у кінці строки
    words = line.split()
    for j in range(len(words)):
        if ord(words[j][-1]) not in range(65, 91) and ord(words[j][-1]) not in range(97, 123):
            words[j] = words[j][:-1]
    for i in words:
        if i.lower() not in dif_words:
            dif_words[i.lower()] = 1
        else:
            dif_words[i.lower()] += 1
for key in sorted(dif_words):
    f.write(key + ' : ' + str(dif_words[key]))
    f.write('\n')
f.close()