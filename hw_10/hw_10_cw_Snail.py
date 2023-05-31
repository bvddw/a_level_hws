# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    result = []
    while(snail_map):
        result.extend(snail_map.pop(0))
        snail_map = list(map(list, zip(*snail_map)))[::-1]
    return result
