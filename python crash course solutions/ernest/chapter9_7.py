"""
9-7: Admin

An administrator is a special kind of user.
Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list of strings like "can add post",
"can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of privileges.
Create an instance of Admin, and call your method.
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
        print("\n" + msg0 + msg1 + msg2 + msg3 + msg4 + "\n")

    def greet_user(self):
        print("\nHi " + self.first_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """A class that inherits from the User and give a user privileges"""

    def __init__(self, first_name, last_name, username, email, location):
        """

        :param first_name:
        :param last_name:
        :param username:
        :param email:
        :param location:
        """
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """shows a users privileges that are in a list"""
        print("The different user privileges for " + self.first_name + " are:")
        for p in self.privileges:
            print("- " + p.title())


admin_1 = Admin("Ernest", "Murray", "ejm", "ejh@hotmail.com", "Leeds")
admin_1.describe_user()
admin_1.privileges = ['can add post', 'can delete post', 'can ban a user']
admin_1.show_privileges()


# class Privileges:
#     """New Privileges class"""
#
#     def __init__(self, privileges):
#         """Single attribute"""
#         self.privileges = privileges
#
#     def show_privileges(self):
#         """shows a users privileges that are in a list"""
#         print("The different user privileges for " + self.first_name + " are:")
#         for p in self.privileges:
#             print("- " + p.title())
#
# new_admin = Privileges("Ernest", "Murray", "ejm", "ejh@hotmail.com", "Leeds")
# new_admin.privileges = ['create', 'delete', 'edit']
# new_admin.show_privileges()

# class User:
#     """Represent a simple user profile."""
#
#     def __init__(self, first_name, last_name, username, email, location):
#         """Initialize the user."""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location.title()
#         self.login_attempts = 0
#
#     def describe_user(self):
#         """Display a summary of the user's information."""
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)
#
#     def greet_user(self):
#         """Display a personalized greeting to the user."""
#         print("\nWelcome back, " + self.username + "!")
#
#     def increment_login_attempts(self):
#         """Increment the value of login_attempts."""
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         """Reset login_attempts to 0."""
#         self.login_attempts = 0
#
#
# class Admin(User):
#     """A user with administrative privileges."""
#
#     def __init__(self, first_name, last_name, username, email, location):
#         """Initialize the admin."""
#         super().__init__(first_name, last_name, username, email, location)
#         self.privileges = []
#
#     def show_privileges(self):
#         """Display the privileges this administrator has."""
#         print("\nPrivileges:")
#         for privilege in self.privileges:
#             print("- " + privilege)
#
#
# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
#
# eric.privileges = [
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
#     ]
#
# eric.show_privileges()
