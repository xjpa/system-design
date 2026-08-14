"""LESSON 04.30: Class design micro-drills.

Run: python course/04_classes_and_objects/30_class_design_drills.py

For each class, separate the questions:

    What must every instance know?  -> attributes created in __init__
    What can every instance do?      -> methods using self
"""


# WORKED EXAMPLE — state belongs to an instance; a method changes it
class Score:
    def __init__(self):
        self.points = 0

    def add(self, amount):
        self.points = self.points + amount


example_score = Score()
example_score.add(3)
assert example_score.points == 3


def expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError("Expected ValueError")


# DRILL 1 — initialize independent instances
class Counter:
    def __init__(self, start=0):
        # TODO: store start as this instance's value.
        pass

    def increment(self):
        # TODO: add one to this instance's value.
        pass


first = Counter()
second = Counter(10)
first.increment()
assert first.value == 1
assert second.value == 10, "Instances must not share changing state"


# DRILL 2 — ask an object to change its own state
class LightSwitch:
    def __init__(self):
        # TODO: every switch starts off.
        pass

    def toggle(self):
        # TODO: change True to False and False to True using `not`.
        pass


switch = LightSwitch()
assert switch.is_on is False
switch.toggle()
assert switch.is_on is True
switch.toggle()
assert switch.is_on is False


# DRILL 3 — protect a rule inside the method that changes state
class InventoryItem:
    def __init__(self, name, quantity):
        # TODO: reject a blank name and a negative quantity.
        # TODO: store the cleaned name and quantity.
        pass

    def remove(self, amount):
        # TODO: reject non-positive amounts and amounts above the quantity.
        # TODO: subtract a valid amount.
        pass

    def is_out_of_stock(self):
        # TODO: return whether quantity is zero.
        pass


item = InventoryItem("Keyboard", 3)
item.remove(2)
assert item.quantity == 1
assert item.is_out_of_stock() is False
item.remove(1)
assert item.is_out_of_stock() is True
expect_value_error(lambda: item.remove(1))
expect_value_error(lambda: InventoryItem(" ", 2))


# TRANSFER CHALLENGE — translate a dictionary-shaped idea into behavior
class ReadingList:
    def __init__(self, owner):
        # TODO: store owner and start with an empty list of titles.
        pass

    def add(self, title):
        # TODO: reject blank or duplicate titles, then append the title.
        pass

    def contains(self, title):
        # TODO: return whether title is in the stored list.
        pass


reading = ReadingList("Ada")
reading.add("Clean Code")
assert reading.contains("Clean Code") is True
assert reading.contains("Refactoring") is False
expect_value_error(lambda: reading.add("Clean Code"))

print("Lesson 04.30 passed: objects own state and the rules that change it.")
