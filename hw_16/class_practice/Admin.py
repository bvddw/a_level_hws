from User import User


class Admin(User):
    def __init__(
            self,
            name: str = '',
            age: int = 18,
            email: str = '',
            address: str = '',
            phone_number: str = '',
            access_level: int = 1
    ) -> None:
        super().__init__(name, age, email, address, phone_number)
        self.access_level = access_level

    def __str__(self):
        super().__str__()
        return f'Admin: {self.name}, age: {self.age}, email: {self.email}, address: {self.address}, phone number: {self.phone_number}, access level: {self.access_level}.'

    def set_access_level(self, level: int) -> bool:
        if 1 <= level <= 2:
            self.access_level = level
            return True
        else:
            print('Invalid level.')
            return False

    def get_access_level(self) -> int:
        return self.access_level
