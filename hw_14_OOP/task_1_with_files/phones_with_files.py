new_file = 'phone_data.txt'  # file for output data

class Phone:  # class phone with fields number and count, where number - phone number, count - number of calls
    number: str = ''  # let the default number be just an empty string
    __count: int = 0  # default number of calls - zero
    name: str = ''  # let the default number be just an empty string

    def set_contact_name(self, name):  # set contact name
        self.name: str = name

    def get_contact_name(self):  # get phone number
        return self.name

    def set_phone_number(self, number):  # set phone number
        self.number: str = number

    def get_phone_number(self):  # get phone number
        return self.number

    def get_number_of_call(self):  # get number of calls
        return self.__count

    def call(self):  # increase the number of calls
        self.__count += 1

# count total number of calls
def amount_of_calls(list_of_phones: list) -> int:  # get total number of calls (for all phones)
    total_count: int = 0
    for phone in list_of_phones:
        total_count += phone.get_number_of_call()
    return total_count


# creating list of phones
def creating_list_of_phones() -> list:
    repeat: bool = True
    while repeat:
        # creating phones
        try:
            number_of_people: int = int(
                input('How many people you want to add to your phone contacts? (enter the number, please) '))

            list_of_phones: list = []
            for _ in range(1, number_of_people + 1):
                # creating phone
                phone: Phone = Phone()
                # get and set contact name
                phone.set_contact_name(input(f'Enter contact name for people {_}: '))
                # get and set phone number
                phone.set_phone_number(input(f'Enter phone number for people {_} (for example "+380123456789"): '))
                list_of_phones.append(phone)  # adding phone to list of phones
            return list_of_phones
            repeat = False
        except ValueError:
            print('Enter the integer number, please.')


# creating list of phones
phones: list = creating_list_of_phones()

# calls for all phones
loop: bool = True
while loop:
    try:
        choice: int = int(input('You want to call someone? (1 - yes, 2 - no) '))
        if choice == 1:
            try:
                number_phone: int = int(input('What phone do you want to call? (1 - first, 2 - second, ...) '))
                if number_phone <= 0:
                    print('You must enter numbers greater than 0.')
                try:
                    phones[number_phone - 1].call()
                except IndexError:
                    print('We do not have that many phones.')
            except ValueError:
                print('You need to enter the number.')
        else:
            loop = False
    except ValueError:
        print('You need to enter the number.')

t_count: int = amount_of_calls(phones)  # total number of calls for all phones
print("\nAmount of calls:", t_count)  # printing total number of calls for all phones

# data to file
with open(new_file, 'w') as file:
    for i, phone in enumerate(phones):
        file.write(f'People {i + 1}:')
        file.write(f"   Contact name: {phone.get_contact_name()}\n")
        file.write(f"   Phone number: {phone.get_phone_number()}\n")
        file.write(f"   Number of calls: {phone.get_number_of_call()}\n")
        file.write("\n")

print("Data is written to the file:", new_file)

print('\nYour contacts:')
for i, n in enumerate(phones):
    print(f'People {i + 1}: \n    name: {n.get_contact_name()}\n    number: {n.get_phone_number()},\n    calls: {n.get_number_of_call()}')
