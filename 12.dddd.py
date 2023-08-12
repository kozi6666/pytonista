class User:
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def print_age(self, message):
        print(message, self.age, self.name)


user1 = User("kuba", 28)
user2 = User("domi", 25)


user1.print_age("Wiek: ")
