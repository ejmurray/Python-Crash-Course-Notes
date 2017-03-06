class Employee:
    """Takes in the first name, last name and annual salary.
       A raise can be added to the persons salary £5000.
    """

    def __init__(self, first_name, last_name):
        """Store the first name, last_name and salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = 0

    def give_raise(self):
        """Increments the salary by £5000."""
        self.salary = self.salary + 5000
