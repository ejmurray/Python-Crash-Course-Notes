"""
9-8: Privileges

Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings
as described in Exercise 9-7. Move the show_privileges() method to this class.
Make a Privileges instance as an attribute in the Admin class.
Create a new instance of Admin and use your method to show its privileges.
"""


class User:
    """Represents a simple user profile"""

    def __init__(self, first_name, last_name, username, email, location):
        """initialise the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print(" Username " + self.username)
        print(" Email " + self.email)
        print(" Location " + self.location)

    def greet_user(self):
        """Display a personalised greeting to the user"""
        print("\nWelcome back, " + self.username + "!")

    def login_attempts(self):
        """Increment the value of the login_attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrator privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialise the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # initialise an empty privileges
        self.privileges = Privileges([])


class Privileges:
    """Stores the privileges associated with an Admin account."""

    def __init__(self, privileges):
        """Initialise the privileges object."""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges this administrator has."""
        for privilege in self.privileges:
            print("- " + privilege)

ernest = Admin('Ernest', 'Murray', 'ejm', 'ej@mail.com', 'UK')
ernest.describe_user()

ernest_privileges = [
    'can reset password',
    'can moderate discussions',
    'can suspend actions'
    ]

ernest.privileges.privileges = ernest_privileges  # need to clarify why there are two calls to privileges here

print("\nThe admin " + ernest.username + " has the following privileges: ")
ernest.privileges.show_privileges()
