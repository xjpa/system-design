"""FOUNDATIONS 06: Lists and loops

Run: python foundations/06_lists_and_loops.py

A list stores several values in order:

    names = ["Ada", "Lin", "Sam"]

A for loop visits each value:

    for name in names:
        print(name)

Read that as: "for each name in names, run the indented instructions."
Start an empty list with [] and add a value with .append(value).
"""


# WORKED EXAMPLE
def double_all(numbers):
    results = []
    for number in numbers:
        results.append(number * 2)
    return results


assert double_all([1, 2, 3]) == [2, 4, 6]


# YOUR TURN 1
def total(numbers):
    answer = 0
    # TODO: loop through numbers and add each number to answer.
    return answer


assert total([2, 3, 4]) == 9, "Add each number to answer inside the loop"
assert total([]) == 0


# YOUR TURN 2
def long_names(names):
    result = []
    # TODO: append only names whose length is greater than 3.
    # len(name) returns the number of characters in a string.
    return result


assert long_names(["Ada", "Grace", "Lin", "James"]) == ["Grace", "James"], (
    "Append names only when len(name) is greater than 3"
)
print("Foundations 06 passed: you processed collections with loops.")
