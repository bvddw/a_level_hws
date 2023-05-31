#  https://www.codewars.com/kata/581e014b55f2c52bb00000f8

#  Decipher this!

def decipher_this(s):
    words = s.split()
    message = ''
    for word in words:
        number = ''
        count = 0
        while count < len(word) and word[count] in '1234567890':  # тільки цифри, щоб отримати по ним літеру
            number += word[count]
            count += 1
        if count == len(word):  # якщо у слові тільки цифри
            message += chr(int(number)) + ' '
        else:
            decipher_word = ''
            decipher_word += chr(int(number))  # знайшли літеру по цифрах
            decipher_word += word[-1]  # друге літера у дешифрованому слові - остання в зашифрованому
            for i in range(count + 1, len(word) - 1):  # додаємо підряд літери у дешифроване слово
                decipher_word += word[i]
            if count < len(word) - 1:  # випадок, коли слово не складається з двох літер
                decipher_word += word[count]
            message += decipher_word + ' '  # додаємо дешифроване слово + пробіл
    return message[:len(message) - 1]  # повертаємо речення, але без останнього пробілу
