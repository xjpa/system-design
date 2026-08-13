"""LESSON 05.40: Object identity and equality

Run: python course/05_python_object_tools/40_identity_and_equality.py

`==` asks whether two values should be considered equal. A class can define the
answer with the special method __eq__:

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id

`isinstance(value, User)` asks whether value is a User object. An ID identifies
one real-world entity even if its editable name changes.

Special method names such as __init__ and __eq__ are called "dunder" methods
(double underscore). Python calls them through normal-looking syntax:

    User(...)          causes __init__ to run
    first == second    causes first.__eq__(second) to run
"""


class User:
    def __init__(self, user_id: int, name: str) -> None:
        self.id = user_id
        self.name = name

    def __eq__(self, other: object) -> bool:
        # TODO: return False if other is not a User.
        # TODO: otherwise return whether the two IDs are equal.
        pass


original = User(1, "Ada")
renamed = User(1, "Ada Lovelace")
different_person = User(2, "Ada")

assert original == renamed, "Users with the same ID should compare equal"
assert original != different_person, "Users with different IDs should not be equal"
assert (original == "not a user") is False
print("Lesson 05.40 passed: entity equality follows stable identity.")
