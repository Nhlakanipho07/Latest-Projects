class Person:
    def __init__(self, name, age, gender, interests=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests if interests is not None else []

    def get_interest_statement(self):

        if len(self.interests) == 1:
            return f"My interest is {self.interests[0]}."
        elif len(self.interests) >= 2:
            return f"My interests are {', '.join(self.interests[:-1])} and {self.interests[-1]}."
        else:
            return "I have no interests."

    def hello(self):
        return f"Hello, my name is {self.name}, my gender is {self.gender} and I am {self.age} years old. {self.get_interest_statement()}"
