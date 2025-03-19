import json
from datetime import datetime


class Visitor:
    def __init__(
        self,
        full_name: str,
        age: int,
        visitor_date: str,
        visitor_time: str,
        comments: str,
        visitor_assistant: str,
    ):
        Visitor.__attribute_validator(
            full_name, age, visitor_date, visitor_time, comments, visitor_assistant
        )
        Visitor.__validate_date_format(visitor_date)
        Visitor.__validate_time_format(visitor_time)

        self.full_name = full_name
        self.age = age
        self.visitor_date = visitor_date
        self.visitor_time = visitor_time
        self.comments = comments
        self.visitor_assistant = visitor_assistant

    def __attribute_validator(
        full_name, age, visitor_date, visitor_time, comments, visitor_assistant
    ):
        assert isinstance(full_name, str), "Visitor name should be a string."
        assert isinstance(age, int), "Visitor age should be an integer."
        assert isinstance(visitor_date, str), "Visitor date should be a string"
        assert isinstance(visitor_time, str), "Visitor time should be a string."
        assert isinstance(comments, str), "Comments should be a string."
        assert isinstance(
            visitor_assistant, str
        ), "Visitor assistant should be a string."

    def __validate_date_format(date):
        try:
            datetime.strptime(date, "%d %B %Y")
            return True
        except ValueError as error_message:
            error_message.args = ("Date format should be: day month_full_name year",)
            raise

    def __validate_time_format(time):
        try:
            datetime.strptime(time, "%Hh%M")
            return True
        except ValueError as error_message:
            error_message.args = (
                "Time should be in 24 hour format with 'h' as the separator.",
            )
            raise

    def __get_file_name(name):
        return f"visitor_{name.replace(' ', '_').lower()}.json"

    def save(self):
        with open(Visitor.__get_file_name(self.full_name), "w") as visitor_data:
            visitor_data.write(json.dumps(self.__dict__))

    @classmethod
    def load(cls, full_name: str):
        assert isinstance(full_name, str), "Visitor name should be a string."

        with open(cls.__get_file_name(full_name), "r") as visitor_data:
            visitor_info = json.load(visitor_data)
        return cls(**visitor_info)
