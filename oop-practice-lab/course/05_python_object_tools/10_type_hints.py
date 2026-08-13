"""LESSON 05.10: Reading type-hint syntax

Run: python course/05_python_object_tools/10_type_hints.py

Professional Python often adds type hints:

    def add(left: int, right: int) -> int:
        return left + right

Read it as:

    left: int       left is expected to be a whole number
    right: int      right is expected to be a whole number
    -> int          the function is expected to return a whole number

The colons inside the parentheses are NOT the colon that starts the function
body. They describe parameters. The final colon starts the indented body.

Hints make intent clearer to humans and checking tools. Python normally does
not enforce them while the program runs.

    name: str              text
    count: int             whole number
    price: float           decimal number
    active: bool           True or False
    items: list[str]       a list of strings
    owner: str | None      either a string or None
    -> None                returns no useful value
"""


# WORKED EXAMPLE
def multiply(left: int, right: int) -> int:
    return left * right


assert multiply(3, 4) == 12


# YOUR TURN: replace the three `object` placeholders with `str`, `bool`, and
# `str`. Do not change the behavior.
def format_user(name: object, active: object) -> object:
    if active:
        return name + " is active"
    return name + " is inactive"


assert format_user("Ada", True) == "Ada is active"
assert format_user("Lin", False) == "Lin is inactive"
assert format_user.__annotations__ == {
    "name": str,
    "active": bool,
    "return": str,
}, "Replace the three object hints with str, bool, and str"
print("Lesson 05.10 passed: type hints do not change working behavior.")
