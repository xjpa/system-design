"""FOUNDATIONS 05: Decisions with if

Run: python foundations/05_conditions.py

An `if` runs indented code only when a condition is True:

    if temperature > 30:
        print("It is hot")

Useful comparisons:

    ==  equal to (two equals signs compare values)
    !=  not equal to
    >   greater than
    <   less than
    >=  greater than or equal to

`else` handles the other case. `elif` means "otherwise, if...".
"""


# WORKED EXAMPLE
def describe_temperature(temperature):
    if temperature > 30:
        return "hot"
    else:
        return "not hot"


assert describe_temperature(35) == "hot"
assert describe_temperature(20) == "not hot"


# YOUR TURN 1
def can_vote(age):
    # TODO: return True when age is at least 18; otherwise return False.
    pass


assert can_vote(18) is True, "18 should be allowed; return True from the if branch"
assert can_vote(30) is True
assert can_vote(17) is False


# YOUR TURN 2
def priority_label(number):
    # TODO: return "high" for numbers 8 or above, "medium" for numbers 4 to 7,
    # and "low" otherwise. Use if, elif, and else.
    pass


assert priority_label(10) == "high", "A number of 8 or more should return 'high'"
assert priority_label(5) == "medium"
assert priority_label(1) == "low"
print("Foundations 05 passed: your functions make decisions.")
