class User:
    def __init__(self, id_user, username):
        """
        :param id_user:
        :param username:
        """
        self.id = id_user
        self.username = username
        self.followers = 0
        self.following = 0
        print("New user being created...")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Mateusz")
print(f"{user_1.username} with id: {user_1.id}")
user_2 = User("002", "Mati")
print(f"{user_2.username} with id: {user_2.id}")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
