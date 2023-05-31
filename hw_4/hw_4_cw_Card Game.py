# https://www.codewars.com/kata/61fef3a2d8fa98021d38c4e5

# Card Game

def card_game(n):
    answer = 0
    while n > 0:
        if n % 4 == 0 and n > 4:  # якщо ділиться на 4, то ми беремо одну карту
            answer += 1
            n -= 1
        elif n % 2 == 0:  # якщо ділиться на 2, але не ділиться на 4, беремо половину
            answer += n // 2
            n //= 2
        else:  # в інших випадках беремо одну карту
            n -= 1
            answer += 1

        if n % 4 == 0 and n > 4:  # ход другого гравця
            n -= 1
        elif n % 2 == 0:
            n //= 2
        else:
            n -= 1

    return answer