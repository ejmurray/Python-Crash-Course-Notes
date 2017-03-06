class Employee:
    """Takes in the first name, last name and annual salary.
       A raise can be added to the persons salary £5000.
    """

    def __init__(self, first_name: object, last_name: object, salary: object) -> object:
        """Store the first name, last_name and salary."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Increments the salary by £5000."""
        self.salary += amount
