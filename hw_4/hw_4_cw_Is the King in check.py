# https://www.codewars.com/kata/5e28ae347036fa001a504bbe

# Is the King in check ?

def king_is_in_check(chessboard : list[list[str]]) -> bool:
    """ do your magic (; """
    string = ''
    for i in range(len(chessboard)):
        for j in range(len(chessboard[i])):
            if chessboard[i][j] == '♔':
                a, b = i, j
                break
    for i in range(len(chessboard)):
        for j in range(len(chessboard[i])):
            if chessboard[i][j] != '♔' and chessboard[i][j] != ' ':
                string = chessboard[i][j]  # ідемо по дошці й перевіряємо кожну фігуру, окрім короля
                m, n = i, j
                if string == '♛':  # якщо фігура - ферзь
                    if a == m and figure_in_line(a, b, n, chessboard) == True:
                        return True
                    if b == n and figure_in_vert(b, a, m, chessboard) == True:
                        return True
                    if abs(a - m) == abs(b - n) and figure_in_diag(a, b, m, n, chessboard) == True:
                        return True
                if string == '♝':  # якщо фігура - слон
                    if abs(a - m) == abs(b - n) and figure_in_diag(a, b, m, n, chessboard) == True:
                        return True
                if string == '♞':  # якщо фігура - кінь
                    if abs(a - m) * abs(b - n) == 2:
                        return True
                if string == '♜':  # якщо фігура - тура
                    if a == m and figure_in_line(a, b, n, chessboard) == True:
                        return True
                    if b == n and figure_in_vert(b, a, m, chessboard) == True:
                        return True
                if string == '♟':  # якщо фігура - пішак
                    if a - m == 1 and abs(b - n) == 1:
                        return True
    return False


def figure_in_line (a, b, n, chessboard):  # перевірка чи є фігура у рядку
    x, y = min(b, n), max(b, n)
    for i in range(x + 1, y):
        if chessboard[a][i] != ' ':
            return False
    return True


def figure_in_vert (b, a, m, chessboard):  # перевірка чи є фігура у стовпці
    x, y = min(a, m), max(a, m)
    for i in range(x + 1, y):
        if chessboard[i][b] != ' ':
            return False
    return True


def figure_in_diag (a, b, m, n, chessboard):  # перевірка чи є фігура у діагоналі
    p, q = min(a, m), max(a, m)
    r = min(b, n)
    if (a - m) * (b - n) > 0:
        for i in range(q - p - 1):
            j = 1
            if chessboard[p + j][r + j] != ' ':
                return False
            j += 1
    if (a - m) * (b - n) < 0:
        for i in range(q - p - 1):
            j = 1
            if chessboard[q - j][r + j] != ' ':
                return False
            j += 1
    return True