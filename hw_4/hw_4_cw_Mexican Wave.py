# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

# Mexican Wave

def wave(people):
    result = []
    for i in range(len(people)):  # ідемо по рядку
        if ord(people[i]) not in range(97, 123):  # якщо цей символ не літера, то пропускаємо цей шаг у циклі
            continue
        result.append(people[:i] + people[i].upper() + people[i + 1:])  # додаємо до хвилі рядок з потрібним uppercase елементом
    return result