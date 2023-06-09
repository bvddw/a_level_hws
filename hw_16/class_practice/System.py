from User import User
from Admin import Admin


class UserSystem:
    def __init__(self):
        self.users: list = []
        self.admins: list = []

    def add_user(self, new_user: User) -> None:
        self.users.append(new_user)

    def add_admin(self, new_admin: Admin) -> None:
        self.admins.append(new_admin)

    def remove_user(self, user: User) -> None:
        if user in self.users:
            self.users.remove(user)

    def remove_admin(self, admin: Admin) -> None:
        if admin in self.admins:
            self.users.remove(admin)

    def get_all_users(self) -> list[User]:
        for i in self.users:
            print(i)
        return self.users

    def get_all_admins(self) -> list[Admin]:
        for i in self.admins:
            print(i)
        return self.admins
