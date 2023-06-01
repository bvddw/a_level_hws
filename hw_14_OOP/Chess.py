class Figure:
    color: bool = True  # 1 (True) - white, 0 (False) - black
    place: tuple = ()

    def change_color(self):
        self.color = not self.color

    def set_place(self, new_place):
        self.place = new_place

    def change_place(self, new_place):
        self.place = new_place


class Pawn(Figure):
    def is_possible_pawn(self, place):
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
    def is_possible_knight(self, place):
        if abs(place[0] - self.place[0]) * abs(place[1] - self.place[1]) == 2:
            return True
        return False


class Bishop(Figure):
    def is_possible_bishop(self, place):
        if abs(place[0] - self.place[0]) == abs(place[1] - self.place[1]) or place[0] - self.place[0] == place[1] - self.place[1]:
            return True
        return False


class Rook(Figure):
    def is_possible_rook(self, place):
        if place[0] == self.place[0] or place[1] == self.place[1]:
            return True
        return False


class Queen(Figure):
    def is_possible_queen(self, place):
        if place[0] == self.place[0] or place[1] == self.place[1] or abs(place[0] - self.place[0]) == abs(place[1] - self.place[1]) or place[0] - self.place[0] == place[1] - self.place[1]:
            return True
        return False


class King(Figure):
    def is_possible_king(self, place):
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


def new_figure(type, place, color):
    figures.append({'figure_type' : type, 'figure_place' : place, 'figure_color': color})


figures: list = []
while True:
    try:
        choice: int = int(input('You want to add figure? (0 - no, any other number - yes) '))
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
        figure: King = King()
        figure.place = cur_place
        figure.color = i['figure_color']
        result: bool = figure.is_possible_king(check_place)
        if result:
            possible_figures.append(i)
    if i['figure_type'] == 2:
        figure: Queen = Queen()
        figure.place = cur_place
        figure.color = i['figure_color']
        result: bool = figure.is_possible_queen(check_place)
        if result:
            possible_figures.append(i)
    if i['figure_type'] == 3:
        figure: Rook = Rook()
        figure.place = cur_place
        figure.color = i['figure_color']
        result: bool = figure.is_possible_rook(check_place)
        if result:
            possible_figures.append(i)
    if i['figure_type'] == 4:
        figure: Bishop = Bishop()
        figure.place = cur_place
        figure.color = i['figure_color']
        result: bool = figure.is_possible_bishop(check_place)
        if result:
            possible_figures.append(i)
    if i['figure_type'] == 5:
        figure: Knight = Knight()
        figure.place = cur_place
        figure.color = i['figure_color']
        result: bool = figure.is_possible_knight(check_place)
        if result:
            possible_figures.append(i)
    if i['figure_type'] == 6:
        figure: Pawn = Pawn()
        figure.place = cur_place
        figure.color = i['figure_color']
        result: bool = figure.is_possible_pawn(check_place)
        if result:
            possible_figures.append(i)

for i, figure_ in enumerate(possible_figures):
    if figure_['figure_color']:
        cur_color: str = 'white'
    else:
        cur_color: str = 'black'
    if figure_['figure_type'] == 1:
        cur_type: str = 'king'
    if figure_['figure_type'] == 2:
        cur_type: str = 'queen'
    if figure_['figure_type'] == 3:
        cur_type: str = 'rook'
    if figure_['figure_type'] == 4:
        cur_type: str = 'bishop'
    if figure_['figure_type'] == 5:
        cur_type: str = 'knight'
    if figure_['figure_type'] == 6:
        cur_type: str = 'pawn'
    print(f"Figure {i + 1}:\n    place: {figure_['figure_place']}\n    type: {cur_type}\n    color: {cur_color}")