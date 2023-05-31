# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(args):
    nums = []
    begin = args[0]
    tmp = []
    result = []
    args.append(args[-1] + 2)
    for i in range(len(args)):
        if len(tmp) == 0:
            tmp.append(str(args[i]))
        else:
            if args[i] == args[i - 1] + 1:
                tmp.append(str(args[i]))
            else:
                if len(tmp) > 2:
                    result.append(tmp[0] + '-' + tmp[-1])
                elif len(tmp) > 0:
                    result.extend(tmp)
                else:
                    result.extend(str(args[i]))
                tmp = [str(args[i])]
    return ','.join(result)