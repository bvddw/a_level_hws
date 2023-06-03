class Figure:
    def __init__(self, color: bool, place: tuple, type: str) -> None:
        self.color = color
        self.place = place
        self.type = type

    def __str__(self) -> str:
        return f"place - {self.place}, type - {self.type}, color - {'white' if self.color else 'black'}."

    def change_color(self) -> None:
        self.color = not self.color

    def change_place(self, new_place: tuple) -> None:
        self.place = new_place


class Pawn(Figure):
    def __init__(self, color: bool, place: tuple, type: str) -> None:
        super().__init__(color, place, type)

    def __str__(self) -> str:
        return super().__str__()

    def is_possible_pawn(self, place: tuple) -> bool:
        if self.color:
            if place[0] == self.place[0]:
                if self.place[1] == 1 and place[1] == 3:
                    return True
                else:
                    if self.place[1] + 1 == place[1]:
                        return True
        else:
            if place[0] == self.place[0]:
                if self.place[1] == 6 and place[1] == 4:
                    return True
                else:
                    if self.place[1] - 1 == place[1]:
                        return True
        return False


class Knight(Figure):
    def __init__(self, color: bool, place: tuple, type: str) -> None:
        super().__init__(color, place, type)

    def __str__(self) -> str:
        return super().__str__()

    def is_possible_knight(self, place: tuple) -> bool:
        if abs(place[0] - self.place[0]) * abs(place[1] - self.place[1]) == 2:
            return True
        return False


class Bishop(Figure):
    def __init__(self, color: bool, place: tuple, type: str) -> None:
        super().__init__(color, place, type)

    def __str__(self) -> str:
        return super().__str__()

    def is_possible_bishop(self, place: tuple) -> bool:
        if abs(place[0] - self.place[0]) == abs(place[1] - self.place[1]) or self.place[1] + self.place[0] == place[1] + place[0]:
            return True
        return False


class Rook(Figure):
    def __init__(self, color: bool, place: tuple, type: str) -> None:
        super().__init__(color, place, type)

    def __str__(self) -> str:
        return super().__str__()

    def is_possible_rook(self, place: tuple) -> bool:
        if place[0] == self.place[0] or place[1] == self.place[1]:
            return True
        return False


class Queen(Figure):
    def __init__(self, color: bool, place: tuple, type: str) -> None:
        super().__init__(color, place, type)

    def __str__(self) -> str:
        return super().__str__()

    def is_possible_queen(self, place: tuple) -> bool:
        if place[0] == self.place[0] or place[1] == self.place[1] or abs(place[0] - self.place[0]) == abs(place[1] - self.place[1]) or self.place[1] + self.place[0] == place[1] + place[0]:
            return True
        return False


class King(Figure):
    def __init__(self, color: bool, place: tuple, type: str) -> None:
        super().__init__(color, place, type)

    def __str__(self) -> str:
        return super().__str__()

    def is_possible_king(self, place: tuple) -> bool:
        if abs(place[0] - self.place[0]) < 2 and abs(place[1] - self.place[1]) < 2:
            return True
        return False


def set_place() -> tuple:
    while True:
        try:
            place: tuple = tuple(map(int, input('Enter two numbers separated by space, both from 0 to 7: ').split()))
            if len(place) != 2 or place[0] not in range(8) or place[1] not in range(8):
                print('You need to enter two numbers separated by space, both from 0 to 7.')
            else:
                break
        except ValueError:
            print('Enter two integer numbers, please')
    return place


def set_type() -> int:
    while True:
        try:
            type: int = int(input('Choose type of your figure, if 1 - king, 2 - queen, 3 - rook, 4 - bishop, 5 - knight, 6 - pawn: '))
            if type not in range(1, 7):
                print('Enter number from 1 to 7')
            else: break
        except ValueError:
            print('Please enter the integer number.')
    return type


def set_color() -> bool:
    while True:
        try:
            color_: int = int(input('Choose color of your figure if 0 - black, any other integer number - white: '))
            break
        except ValueError:
            print('Please enter the integer number.')
    return bool(color_)


def new_figure(type: int, place: tuple, color: bool) -> None:
    figures.append({'figure_type' : type, 'figure_place' : place, 'figure_color': color})


figures: list = []
while True:
    try:
        choice: int = int(input('Do you want to add figure? (0 - no, any other number - yes) '))
        if choice:
            place_: tuple = set_place()
            type: int = set_type()
            color: bool = set_color()
            new_figure(type, place_, color)
        else:
            break
    except ValueError:
        print('Enter integer number please.')

print('Now let set place on the board for checking: ')
check_place: tuple = set_place()
possible_figures: list = []

for i in figures:
    cur_place: tuple = i['figure_place']
    if i['figure_type'] == 1:
        figure: King = King(i['figure_color'], cur_place, 'king')
        result: bool = figure.is_possible_king(check_place)
        if result:
            possible_figures.append(figure)
    if i['figure_type'] == 2:
        figure: Queen = Queen(i['figure_color'], cur_place, 'queen')
        result: bool = figure.is_possible_queen(check_place)
        if result:
            possible_figures.append(figure)
    if i['figure_type'] == 3:
        figure: Rook = Rook(i['figure_color'], cur_place, 'rook')
        result: bool = figure.is_possible_rook(check_place)
        if result:
            possible_figures.append(figure)
    if i['figure_type'] == 4:
        figure: Bishop = Bishop(i['figure_color'], cur_place, 'bishop')
        result: bool = figure.is_possible_bishop(check_place)
        if result:
            possible_figures.append(figure)
    if i['figure_type'] == 5:
        figure: Knight = Knight(i['figure_color'], cur_place, 'knight')
        result: bool = figure.is_possible_knight(check_place)
        if result:
            possible_figures.append(figure)
    if i['figure_type'] == 6:
        figure: Pawn = Pawn(i['figure_color'], cur_place, 'pawn')
        result: bool = figure.is_possible_pawn(check_place)
        if result:
            possible_figures.append(figure)

print(f'\nFigures, what can stand on position {check_place}:')
for i, figure_ in enumerate(possible_figures):
    print(f"Figure {i + 1}: {figure_}")