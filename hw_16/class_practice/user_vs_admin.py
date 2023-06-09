from User import User
from Admin import Admin
from System import UserSystem


# Create a UserSystem instance
system_ad_us: UserSystem = UserSystem()

# Create regular users
while True:
    try:
        choice: int = int(input('Do you want to add new regular user?\n1. YES\n2. NO\n'))
        match choice:
            case 1:
                new_user: User = User()
                new_name: str = input('Enter user name: ')
                new_user.set_name(new_name)
                while True:
                    try:
                        new_age: int = int(input('Enter user age: '))
                        if new_user.set_age(new_age):
                            break
                    except ValueError:
                        print('You need to enter the integer number.')
                while True:
                    new_email: str = input('Enter user email: ')
                    if new_user.set_email(new_email):
                        break
                new_address: str = input('Enter user address: ')
                new_user.set_address(new_address)
                while True:
                    new_number: str = input('Enter user phone number: ')
                    if new_user.set_phone_number(new_number):
                        break
                system_ad_us.add_user(new_user)
            case 2:
                print('All users added.')
                break
            case _:
                print('You need to enter 1 or 2.')
    except ValueError:
        print('You need to enter 1 or 2')

# Create regular users
while True:
    try:
        choice: int = int(input('Do you want to add new admin?\n1. YES\n2. NO\n'))
        match choice:
            case 1:
                new_admin: Admin = Admin()
                new_name: str = input('Enter admin name: ')
                new_admin.set_name(new_name)
                while True:
                    try:
                        new_age: int = int(input('Enter admin age: '))
                        if new_admin.set_age(new_age):
                            break
                    except ValueError:
                        print('You need to enter the integer number.')
                while True:
                    new_email: str = input('Enter admin email: ')
                    if new_admin.set_email(new_email):
                        break
                new_address: str = input('Enter admin address: ')
                new_admin.set_address(new_address)
                while True:
                    new_number: str = input('Enter admin phone number: ')
                    if new_admin.set_phone_number(new_number):
                        break
                while True:
                    try:
                        new_access_level: int = int(input('Choose access level:\n1. Admin\n2. Super Admin\n'))
                        if new_admin.set_access_level(new_access_level):
                            break
                    except ValueError:
                        print('You need to enter 1 or 2.')
                system_ad_us.add_admin(new_admin)
            case 2:
                print('All admins added.')
                break
            case _:
                print('You need to enter 1 or 2.')
    except ValueError:
        print('You need to enter 1 or 2')
print('\nUsers:')
system_ad_us.get_all_users()
print('\nAdmins:')
system_ad_us.get_all_admins()
