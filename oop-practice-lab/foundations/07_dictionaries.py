"""FOUNDATIONS 07: Dictionaries

Run: python foundations/07_dictionaries.py

A dictionary stores key/value pairs:

    user = {"name": "Ada", "role": "developer"}

Read a value by its key:

    user["name"]          gives "Ada"

Change or add a value:

    user["role"] = "admin"
    user["active"] = True

Dictionaries are useful, but later you will see why classes can be clearer when
data and behavior belong together.
"""


# WORKED EXAMPLE
def full_name(user):
    return user["first_name"] + " " + user["last_name"]


ada = {"first_name": "Ada", "last_name": "Lovelace"}
assert full_name(ada) == "Ada Lovelace"


# YOUR TURN 1
def mark_complete(task):
    # TODO: change the "complete" value to True, then return task.
    pass


task = {"title": "Learn dictionaries", "complete": False}
updated_task = mark_complete(task)
assert updated_task is not None, "Return task at the end of mark_complete"
assert updated_task["complete"] is True, "Set task['complete'] to True"


# YOUR TURN 2
def count_roles(users):
    counts = {"developer": 0, "designer": 0}
    # TODO: loop through users. Increase the matching role count by 1.
    # Example: counts["developer"] = counts["developer"] + 1
    return counts


team = [
    {"name": "Ada", "role": "developer"},
    {"name": "Lin", "role": "designer"},
    {"name": "Sam", "role": "developer"},
]
assert count_roles(team) == {"developer": 2, "designer": 1}, (
    "Increase the count matching each user's role"
)
print("Foundations 07 passed: you used structured key/value data.")
