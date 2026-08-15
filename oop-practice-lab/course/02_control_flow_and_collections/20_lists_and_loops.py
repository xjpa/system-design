"""LESSON 02.20: Lists and loops

Run: python course/02_control_flow_and_collections/20_lists_and_loops.py

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


# YOUR TURN 3
def count_occurrences(items, target):
    count = 0
    # TODO: add 1 to count each time an item equals target.
    return count


assert count_occurrences(["bug", "api", "bug"], "bug") == 2, (
    "Increase count whenever an item equals target"
)
assert count_occurrences(["bug", "api"], "docs") == 0
assert count_occurrences([], "bug") == 0


# YOUR TURN 4
def contains(items, target):
    # TODO: loop through items. Return True as soon as an item equals target.
    # If the loop finishes without finding target, return False.
    return False


assert contains(["open", "closed", "blocked"], "open") is True, (
    "Return True when target appears in the list"
)
assert contains(["open", "closed", "blocked"], "blocked") is True
assert contains(["open", "closed"], "missing") is False
assert contains([], "open") is False


# YOUR TURN 5
def running_totals(numbers):
    result = []
    current_total = 0
    # TODO: add each number to current_total, then append current_total.
    return result


assert running_totals([2, 3, 4]) == [2, 5, 9], (
    "Append the new total after processing each number"
)
assert running_totals([5, -2, 1]) == [5, 3, 4]
assert running_totals([]) == []


# YOUR TURN 6 — CHALLENGE
def largest_number(numbers):
    # This exercise expects a non-empty list. numbers[0] is its first value.
    largest = numbers[0]
    # TODO: replace largest whenever the current number is greater.
    return largest


assert largest_number([4, 9, 2, 7]) == 9, (
    "Keep the greatest number seen while moving through the list"
)
assert largest_number([6]) == 6
assert largest_number([-8, -3, -10]) == -3, (
    "Start with the first list value so all-negative lists work"
)

print("Lesson 02.20 passed: you processed collections with loops.")
