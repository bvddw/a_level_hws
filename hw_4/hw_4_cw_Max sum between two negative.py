#  https://www.codewars.com/kata/6066ae080168ff0032c4107a

#  Max sum between two negatives

def max_sum_between_two_negatives(arr):
    sum_between = 0  # сума між двома від'ємними
    max_sum = 0   # максимальна сума між двома від'ємними
    count = 0  # лічільник від'ємних чисел
    while len(arr) and arr[0] >= 0: # видаляємо усе до першого від'ємного числа
        arr.pop(0)
    for i in range(len(arr)):  # ідемо по масиву, рахуємо суму між двома від'ємними, перевіряючи чи є вона максимальною
        if arr[i] >= 0:
            sum_between += arr[i]
        if arr[i] < 0:
            count += 1
            max_sum = sum_between if max_sum < sum_between else max_sum
            sum_between = 0
    if count < 2: return -1
    return max_sum