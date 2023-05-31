# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def strip_comments(strng, markers):
    answer = []
    strings = strng.split('\n')
    for string in strings:
        tmp_ans = ''
        count = 0
        skip = 0
        for i in range(len(string)):
            if skip == 1:
                continue
            if string[i] == '/':
                if string[i + 1] == 't':
                    count += 4
                    continue
                    skip = 1
            if string[i] in markers:
                break
            elif string[i] == ' ':
                count += 1
            else:
                tmp_ans += ' ' * count + string[i]
                count = 0
        answer.append(tmp_ans)
    return '\n'.join(answer)