"""
C. Place for a Selfie
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

The universe is a coordinate plane. There are n space highways, each of which is a straight line y = k * x passing through the origin (0, 0).
Also, there are m asteroid belts on the plane, which we represent as open upwards parabolas, i.e. graphs of functions y=a * x^2 + b * x + c, where a > 0.

You want to photograph each parabola. To do this, for each parabola you need to choose a line that does not intersect this parabola and does not touch it.
You can select the same line for different parabolas. Please find such a line for each parabola, or determine that there is no such line.

INPUT
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 104). The description of the test cases follows.
The first line of each test case contains 2 integers n and m (1 ≤ n, m ≤ 105) — the number of lines and parabolas, respectively.
Each of the next n lines contains one integer k (|k| ≤ 108), denoting a line that is described with the equation y=kx. The lines are not necessarily distinct, k can be equal to 0.
Each of the next m lines contains 3 integers a, b, and c (a, |b|, |c| ≤ 108, a > 0) — coefficients of equations of the parabolas a * x ^ 2 + b * x + c. The parabolas are not necessarily distinct.
It is guaranteed that the sum n over all test cases does not exceed 105, and the sum m over all test cases also does not exceed 105.

OUTPUT
For each test case, output the answers for each parabola in the given order.
If there is a line that does not intersect the given parabola and doesn't touch it, print on a separate line the word "YES", and then on a separate line the number k — the coefficient of this line.
If there are several answers, print any of them. If the line does not exist, print one word "NO".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

The empty lines in the output in the example are given only for illustration, you do not need to output them (but you can).
"""


def bin_search(k_arr, abc_, start, end):
    lenght = end - start
    if lenght == 0:
        return start
    mid = 0 if lenght // 2 - 1 < 0 else lenght // 2 - 1
    mid += start
    if abc_[1] < k_arr[mid]:
        return bin_search(k_arr, abc_, start, mid)
    else:
        return bin_search(k_arr, abc_, mid + 1, end)


t = int(input())
for x in range(t):
    n, m = list(map(int, input().split()))
    k_array = []
    for i in range(n):
        k_array.append(int(input()))
    k_array = sorted(k_array)
    abc_array = []
    for i in range(m):
        abc_array.append(list(map(int, input().split())))
    for current_abc in abc_array:
        check = bin_search(k_array, current_abc, 0, len(k_array) - 1)
        if (current_abc[1] - k_array[check]) ** 2 < 4 * current_abc[0] * current_abc[2]:
            print('YES')
            print(k_array[check])
        elif check > 0 and (current_abc[1] - k_array[check - 1]) ** 2 < 4 * current_abc[0] * current_abc[2]:
            print('YES')
            print(k_array[check - 1])
        elif check < n - 1 and (current_abc[1] - k_array[check + 1]) ** 2 < 4 * current_abc[0] * current_abc[2]:
            print('YES')
            print(k_array[check + 1])
        else:
            print('NO')
    print()
