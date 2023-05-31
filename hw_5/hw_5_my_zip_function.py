def my_zip(*args):
    """
    Кастомна zip-функція, яка буде об'єднувати відповідні елементи у строку, а не у кортежі

    Аргумент:
        у якості аргументу може бути один або декілька ітерованих об'єктів

    Що функція повертає:
        Лист строк, кожна з яких є об'єднанням відповідних елементів, які ми взяли з ітерованих об'єктів.
        Довжина кожної строки буде дорівнювати мінімальній кількості елементів серед об'єктів, введених користувачем.
    """
    result = []
    for elements in zip(*args):
        result.append(''.join(str(e) for e in elements))
    return result


num_iterables = int(input("Enter number of iterables: "))  # отримуємо кількість об'єктів від користувача
iterables = []
for i in range(num_iterables):  # об'єднуємо в один аргумент функції
    iterable = input(f"Enter elements for iterable {i+1} (with spaces between elements): ")
    iterables.append(list(map(str, iterable.split())))

print(f"Result: {', '.join(my_zip(*iterables))}.")