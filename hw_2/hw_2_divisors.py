num = int(input('Enter a number: '))
num_cpy = num
divisors = []
discharges = []
print('Even number.') if not num % 2 else print('Odd number.')
print('Good number! (if % 5, %3 == 0, % 10 != 0)') if not num % 5 and not num % 3 and num % 10 else print('Not good number.')
for i in range(1, num // 2 + 1):
    if not num % i:
        divisors.append(i)
    else:
        i += 1
divisors.append(num)
print(f"Divisors of your number: {', '.join([str(num) for num in divisors])}.")
k = 0
while num > 0:
    discharges.append(str(num % 10) + ' * ' + str(10 ** k))
    k += 1
    num //= 10
print(f'{num_cpy} = {" + ".join(discharges)}')