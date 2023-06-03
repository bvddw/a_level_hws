import psycopg2
from settings import host, user, password, db, port

new_database = 'phone_numbers'
new_table = 'phones'
new_columns = False


class Phone:  # class phone with fields number and count, where number - phone number, count - number of calls
    # initialization class (Phone) representative
    def __init__(self, name, number, count):
        self.name = name
        self.number = number
        self.__count = count

    # magic method for print data
    def __str__(self):
        return f'name - {self.name}, number - {self.number}, calls - {self.__count}.'

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
    while True:
        # creating phones
        try:
            number_of_phones: int = int(
                input('How many numbers you want to add to your phone contacts? (enter the number, please) '))
            list_of_phones: list = []
            for p in range(1, number_of_phones + 1):
                # get contact name
                name = input(f'Enter contact name for {p} phone: ')
                # get phone number
                phone_number = input(f'Enter phone number for {p} phone (for example "+380123456789"): ')
                # create phone
                phone: Phone = Phone(name, phone_number, 0)
                list_of_phones.append(phone)  # adding phone to list of phones
            return list_of_phones
        except ValueError:
            print('Enter the integer number, please.')



try:
    connect = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db
    )

    connect.set_session(autocommit=True)

    with connect.cursor() as cursor:
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{new_database}'")
        db_exists = cursor.fetchone()[0]

        if not db_exists:
            cursor.execute(f'CREATE DATABASE {new_database};')
            print(f'Create Database!')

    connect = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=new_database
    )

    connect.set_session(autocommit=True)

    with connect.cursor() as cursor:
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{new_table}')")
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            cursor.execute(f'''CREATE TABLE {new_table} (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(20) NOT NULL,
                        phone VARCHAR(20) NOT NULL,
                        calls INTEGER NOT NULL);''')

        # creating list of phones
        phones: list = creating_list_of_phones()

        # calls for all phones
        while True:
            try:
                choice: int = int(input('You want to call someone? (1 - yes, any other number - no) '))
                if choice == 1:
                    try:
                        number_phone: int = int(input('What phone do you want to call? (1 - first,  2 - second, ...) '))
                        if number_phone <= 0:
                            print('You must enter numbers greater than 0.')
                        try:
                            phones[number_phone - 1].call()
                        except IndexError:
                            print('We do not have that many phones.')
                    except ValueError:
                        print('You need to enter the number.')
                else:
                    break
            except ValueError:
                print('You need to enter the number.')

        t_count: int = amount_of_calls(phones)  # total number of calls for all phones
        print("\nAmount of calls:", t_count)  # printing total number of calls for all phones

        for i in phones:
            cursor.execute(f"INSERT INTO {new_table} (name, phone, calls) VALUES (%s, %s, %s);", (i.name, i.number, i.get_number_of_call()))

        print("Data is updated!")

        # output phone contacts
        print('\nYour contacts:')
        for i, n in enumerate(phones):
            print(f'Phone number {i + 1}: {n}')

except Exception as e:
    print('Error:', e)

finally:
    if connect:
        connect.close()
        print('Connection end!')
