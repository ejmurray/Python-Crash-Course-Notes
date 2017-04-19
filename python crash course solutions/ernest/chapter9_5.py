"""
9-5: Login Attempts

Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166).
Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0.
"""


class User:
    """Typical entries in a user profile"""

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        msg0 = "User Information: " + "\n"
        msg1 = "Name: " + self.first_name + " " + self.last_name + "\n"
        msg2 = "Username: " + self.username + "\n"
        msg3 = "Email: " + self.email + "\n"
        msg4 = "Location: " + self.location
        print("\n" + msg0 + msg1 + msg2 + msg3 + msg4)

    def greet_user(self):
        print("\nHi " + self.first_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

increment = User("Ernest", "Murray", "ejm", "ejmurray247@hotmail.com", "UK")
increment.describe_user()
increment.greet_user()
print("\nMaking three login attempts.......")
increment.increment_login_attempts()
increment.increment_login_attempts()
increment.increment_login_attempts()
print("Login attempts: " + str(increment.login_attempts))

print("\nReset login attempts.......")
print("\nReset login attempts.......")
increment.reset_login_attempts()
print("Login attempts: " + str(increment.login_attempts))
