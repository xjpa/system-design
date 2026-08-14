"""LESSON 02.40: Control-flow and collection pattern drills.

Run: python course/02_control_flow_and_collections/40_problem_solving_patterns.py

Most beginner collection problems are variations of four patterns:
filter, transform, accumulate, and look up. Implement them with ordinary loops
first; compact comprehensions can come later.
"""


# WORKED EXAMPLE — filter values with an explicit loop
def even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


assert even_numbers([1, 2, 3, 4]) == [2, 4]


# PATTERN 1 — classify with conditionals
def ticket_price(age):
    # TODO: return 0 for under 5, 10 for under 18, otherwise 20.
    pass


assert ticket_price(4) == 0
assert ticket_price(12) == 10
assert ticket_price(30) == 20


# PATTERN 2 — filter: keep only matching items
def positive_numbers(numbers):
    result = []
    # TODO: loop over numbers and append only values greater than zero.
    return result


assert positive_numbers([-2, 0, 3, 5]) == [3, 5]
assert positive_numbers([]) == []


# PATTERN 3 — transform: produce one new item for every old item
def uppercase_all(words):
    result = []
    # TODO: append word.upper() for every word.
    return result


assert uppercase_all(["api", "bug"]) == ["API", "BUG"]


# PATTERN 4 — accumulate: combine many items into one result
def total(numbers):
    result = 0
    # TODO: add every number to result.
    return result


assert total([4, 6, 10]) == 20
assert total([]) == 0


# PATTERN 5 — dictionary lookup with a fallback
def role_for(user_name, roles):
    # TODO: return the stored role, or "guest" when the name is absent.
    # Hint: dictionaries have a .get(key, fallback) method.
    pass


assert role_for("Ada", {"Ada": "admin"}) == "admin"
assert role_for("Lin", {"Ada": "admin"}) == "guest"


# PATTERN 6 — frequency table: count repeated values
def count_words(words):
    counts = {}
    # TODO: for each word, read its current count (default 0) and add 1.
    return counts


assert count_words(["bug", "api", "bug"]) == {"bug": 2, "api": 1}


# TRANSFER CHALLENGE — filter and accumulate in the same traversal
def paid_order_total(orders):
    """Add `amount` only for dictionaries whose `paid` value is True."""
    result = 0
    # TODO: loop, decide, and accumulate.
    return result


orders = [
    {"amount": 20, "paid": True},
    {"amount": 50, "paid": False},
    {"amount": 30, "paid": True},
]
assert paid_order_total(orders) == 50

print("Lesson 02.40 passed: filter, transform, accumulate, and lookup.")
