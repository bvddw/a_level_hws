# https://www.codewars.com/kata/583a8bde28019d615a000035

def find_odd_names(lst):
    odd_names = []
    for i in lst:
        suma = 0
        for ch in i['firstName']:
            suma += ord(ch)
        if suma % 2:
            odd_names.append(i)
    return odd_names