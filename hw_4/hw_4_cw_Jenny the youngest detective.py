#  https://www.codewars.com/kata/58b972cae826b960a300003e

#  Jenny the youngest detective

def missing(nums, s):
    delete_spaces = s.split()
    no_spaces = ''.join(delete_spaces)  # прибрали усі пробіли
    nums.sort()  # відсортували лист чисел
    mission = ''
    if len(no_spaces) - 1 < nums[2]:  # якщо не розшифрувати місію
        return 'No mission today'
    for i in nums:  # беремо три літери, і отримуємо місію
        mission += no_spaces[i].lower()
    return mission
