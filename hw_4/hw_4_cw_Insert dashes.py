# https://www.codewars.com/kata/55960bbb182094bc4800007b

# Insert dashes

def insert_dash(num):
    num = str(num)  # перетворюємо число на рядок для зручності
    modified_num = num[0]
    odds = '13579'  # рядок тільки з непарних чисел
    for i in range(len(num) - 1):  # ідемо по рядку
        if num[i] in odds and num[i + 1] in odds:  # додаємо тире, якщо поруч стоять два непарних числа
            modified_num += '-'
        modified_num += num[i + 1]
    return modified_num
