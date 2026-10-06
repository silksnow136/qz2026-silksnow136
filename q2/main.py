import json


class UserManager:
    def __init__(self):
        self.users = []
        self.userCount = 0

    def add_user(self, username, age):
        self.userCount += 1
        user = {"id": self.userCount, "username": username, "age": age}
        self.users.append(user)

    def get_users(self, id):
        for user in self.users:
            if user["id"] == id:
                return user
        return None

    def update_age(self, id, new_age):
        user = self.get_users(id)
        if user:
            user["age"] = new_age
            return True
        return False

    def remove_user(self, id):
        user = self.get_users(id)
        if user:
            self.users.remove(user)
            self.userCount -= 1
            return True
        return False

    def list_users(self):
        return self.users

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.users, f)

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            self.users = json.load(f) 