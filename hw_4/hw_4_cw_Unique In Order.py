# https://www.codewars.com/kata/54e6533c92449cc251001667

# Unique In Order

def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    unique = [sequence[0]]  # додаємо перший елемент послідовності у відповідь
    for i in range(1, len(sequence)):  # ідемо по послідовності, починаючи з другого елементу
        if sequence[i] != unique[-1]:  # якщо останній елемент шуканої послідовності, не збігається з елементом sequence[i], то додаємо sequence[i] у відповідь
            unique.append(sequence[i])
    return unique
