def spam(number):
    '''Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''
    result = ''  # here we will save result
    for i in range(number):  # repeat as many times as needed
        result += 'bulochka'  # adding 'bulochka' to the result as many times as needed
    return result  #  return result


def my_sum(list_of_numbers):

    """Function receives a list with integer numbers,
    should return its sum as an integer. Do not use built in summarize functions.
    :param list

    Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
    Не использовать встроенные функции суммирования.
    
    """
    #  ...wite your code here
    suma = 0  # sum of elements in array
    for i in list_of_numbers:
        suma += i  # adding every element to the sum
    return suma  # return result


def shortener(string):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


    """
    #  ...wite your code here
    string = string.split()  # separate string by spaces, now we have array, where each element is one word
    for i in range(len(string)):  # checking every element in array
        if len(string[i]) > 6:  # if length more than 6
            string[i] = string[i][:6] + '*'  # changing word: take only first 6 characters and add '*' to the end
    return ' '.join(string)  # return result as string by using join with ' ' - spaces between each to elements


def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    #  ...wite your code here
    count = 0  # counter of correct words (length is at least 2 and the first character is equal to the last)
    for i in words:  # checking every word in array of words
        if len(i) > 1 and i[0] == i[-1]:  # if length is at least 2 and the first character is equal to the last, we're adding 1 to the counter
            count += 1
    return count  # return answer
