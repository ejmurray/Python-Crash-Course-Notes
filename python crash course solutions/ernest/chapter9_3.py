class User:
    """Typical enteries in a user profile"""

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        msg0 = "User Information: " + "\n"
        msg1 = "Name: " + self.first_name + " " + self.last_name + "\n"
        msg2 = "Username: " + self.username + "\n"
        msg3 = "Email: " + self.email + "\n"
        msg4 = "Location: " + self.location
        print("\n" + msg0 + msg1 + msg2 + msg3 + msg4)

    def greet_user(self):
        print("\n" + "Hi " + self.first_name + "!")

alan = User("Ernest", "Murray", "ejm", "ejm@mail.com", "UK")
alan.describe_user()
alan.greet_user()

ed = User("Ed", "Moses", "egm", "egm@mail.com", "UK")
ed.describe_user()
ed.greet_user()

gaynor = User("Gaynor", "Pratt", "gap", "gap@mail.com", "UK")
gaynor.describe_user()
gaynor.greet_user()

busta = User("Busta", "Rhymes", "lotns", "lotns@mail.com", "UK")
busta.describe_user()
busta.greet_user()


# code from the website https://goo.gl/1Od6Qm

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()
