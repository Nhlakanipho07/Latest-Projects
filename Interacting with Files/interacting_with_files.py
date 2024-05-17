import json
import os


class Visitor:
    def __init__(
        self,
        id: int,
        full_name: str,
        age: int,
        visitor_date: str,
        visitor_time: str,
        comments: str,
        visitor_assistant: str,
    ):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.visit_date = visitor_date
        self.visit_time = visitor_time
        self.comments = comments
        self.visitor_assistant = visitor_assistant

        if not isinstance(self.id, int):
            raise TypeError(
                "Invalid type, please enter the visitor's id as an integer."
            )
        if not isinstance(self.full_name, str):
            raise TypeError(
                "Invalid type, please enter the visitor's full name as a string."
            )
        if not isinstance(self.age, int):
            raise TypeError(
                "Invalid type, please enter the vistor's age as an integer."
            )
        if not isinstance(self.visit_date, str):
            raise TypeError(
                "Invalid type, please enter the date the visitor visited as a string."
            )
        if not isinstance(self.visit_time, str):
            raise TypeError(
                "Invalid type, please the time the visitor visited as a string."
            )
        if not isinstance(self.comments, str):
            raise TypeError("Invalid type, please enter comments as a string.")
        if not isinstance(self.visitor_assistant, str):
            raise TypeError(
                "Invalid type, please enter the name of the person who assisted the visitor as a string."
            )

    def save(self):
        visitor_info = {
            "id": self.id,
            "full_name": self.full_name,
            "age": self.age,
            "visitor_date": self.visit_date,
            "visitor_time": self.visit_time,
            "comments": self.comments,
            "visitor_assistant": self.visitor_assistant,
        }

        with open(f"visitor_{self.id}.json", "w") as visitor_data:
            visitor_data.write(json.dumps(visitor_info))

    @classmethod
    def load(cls, visitor_id: int) -> int:
        if not isinstance(visitor_id, int):
            raise TypeError("Invalid type, please enter the visitor's id as an integer")

        if os.path.isfile(f"visitor_{visitor_id}.json"):
            with open(f"visitor_{visitor_id}.json", "r") as visitor_data:
                visitor_data = json.load(visitor_data)
                visitor_data = cls(**visitor_data)

                return visitor_data
