#  https://www.codewars.com/kata/55c3026406402936bc000026

#  Insert Dashes 2

def insert_dash2(num):
    num = str(num)  # перетворюємо число на рядок для зручності
    modified_num = num[0]
    odd = '13579'  # рядок тільки з непарних чисел
    even = '2468'  # рядок тільки з парних чисел (0 сюди не відноситься за умовою)
    for i in range(len(num) - 1):  # ідемо по рядку
        if num[i] in odd and num[i + 1] in odd:  # додаємо тире, якщо поруч стоять два непарних числа
            modified_num += '-'
        elif num[i] in even and num[i + 1] in even:  # додаємо *, якщо поруч стоять два парних числа
            modified_num += '*'
        modified_num += num[i + 1]
    return modified_num
