class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def changePassword(self, oldPassword, newPassword):
        if oldPassword == self.password:
            self.newPassword = newPassword
            print("password chanhed")
        else:
            print("invalid password")

user = User("adamkowalski", "admin12345")
user.changePassword("peg2", "peg3")
user.changePassword("admin12345", "peg3")