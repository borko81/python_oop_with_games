from typing import ClassVar
from dataclasses import dataclass, field


# order use for __lt__ and more magic function
# frozen is use for freeze variable

@dataclass(order=True)
class Person:
    firstname: str
    lastname: str
    age: int
    message: ClassVar[str] = "Hello"
    skills: list = field(default_factory=list)

    @staticmethod
    def greeting():
        print("Hello there")

    def __repr__(self):
        return f"{self.age} Person.message"


person_one = Person(*'First Last 41'.split())
person_two = Person(*'First Last 40'.split())

persons = [person_one, person_two]
persons = sorted(persons)

person_one.skills.append('One')
print(person_one.skills)
