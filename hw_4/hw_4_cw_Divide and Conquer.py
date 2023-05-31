#  https://www.codewars.com/kata/57eaec5608fed543d6000021

#  Divide and Conquer

def div_con(x):
    result = 0
    for i in x:  # ідемо по листу
        if type(i) == type(''):  # якщо тип str, то віднімаємо число від результату
            result -= int(i)
        else:  # якщо тип int, то додаємо число до результату
            result += i
    return result
