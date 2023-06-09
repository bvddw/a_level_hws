class User:
    def __init__(
            self,
            name: str = '',
            age: int = 18,
            email: str = '',
            address: str = '',
            phone_number: str = '',
    ) -> None:
        self.name: str = name
        self.age: int = age
        self.email: str = email
        self.address: str = address
        self.phone_number: str = phone_number

    def __str__(self) -> str:
        return f'User: {self.name}, age: {self.age}, email: {self.email}, address: {self.address}, phone number: {self.phone_number}.'

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def get_email(self) -> str:
        return self.email

    def set_name(self, new_name: str) -> bool:
        if len(new_name) > 256:
            print('invalid name')
            return False
        else:
            self.name = new_name
            return True

    def set_age(self, new_age: int) -> bool:
        if 18 <= new_age <= 120:
            self.age = new_age
            return True
        else:
            print('invalid age')
            return False

    def set_email(self, new_email: str) -> bool:
        if '@' in new_email:
            self.email = new_email
            return True
        else:
            print('invalid email')
            return False

    def set_address(self, new_address: str) -> None:
        self.address = new_address

    def set_phone_number(self, new_phone_number: str) -> bool:
        if new_phone_number.startswith("+380"):
            self.phone_number = new_phone_number
            return True
        else:
            print('invalid phone_number')
            return False
