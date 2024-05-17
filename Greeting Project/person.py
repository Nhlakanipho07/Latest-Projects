class Person:
    def __init__(self, name: str, age: int, gender: str, interests: list = "none"):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

        self.__attribute_checker()

    def __attribute_checker(self):
        if not isinstance(self.name, str):
            raise TypeError("Invalid type, please enter the name as a string.")
        if not isinstance(self.age, int):
            raise TypeError("Invalid type, please enter the age as an integer.")
        if not isinstance(self.gender, str):
            raise TypeError("Invalid type, please enter the gender as a string.")
        if not isinstance(self.interests, (list, str)):
            raise TypeError("Invalid type, please enter the interest(s) as a list.")

    def __interests_statement(self):
        interests = None
        many_interests = ""

        if self.interests != "none":
            count_interests = len(self.interests)
        else:
            count_interests = "none"

        if count_interests == "none":
            interests = "I have no interests."
        elif count_interests == 1:
            interests = f"My interest is {self.interests[0]}."
        elif count_interests == 2:
            interests = f"My interests are {self.interests[0]} and {self.interests[1]}."
        elif count_interests >= 3:
            for interest in range(1, len(self.interests) - 1):
                many_interests += f", {self.interests[interest]}"
            interests = f"My interests are {self.interests[0]}{many_interests} and {self.interests[-1]}."

        return interests

    def hello(self):
        interests = self.__interests_statement()
        hello = f"Hello, my name is {self.name}, my gender is {self.gender} and I am {self.age} years old. {interests}"
        return hello
