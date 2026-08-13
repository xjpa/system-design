"""LESSON 04.10: Why classes exist

Run: python course/04_classes_and_objects/10_from_dictionary_to_class.py

With a dictionary, any caller can create nonsense or change data directly:

    account = {"owner": "Ada", "balance": 100}
    account["balance"] = -999999

A class is a blueprint for objects. It keeps related data and functions
(called methods) together and controls how its state changes.

    class Counter:
        def __init__(self, starting_value):
            self.value = starting_value

        def increase(self):
            self.value = self.value + 1

Important syntax:

    class Counter:       define a class named Counter
    __init__             runs when a new object is created
    self                 the particular object receiving the method call
    self.value           an attribute stored on that object
    Counter(5)           create an object; 5 becomes starting_value
    counter.increase()   call a method on that object

`self` is written in a method definition, but you do not pass it explicitly.
Python supplies it from the object before the dot.
"""


# WORKED EXAMPLE
class Counter:
    def __init__(self, starting_value):
        self.value = starting_value

    def increase(self):
        self.value = self.value + 1


first = Counter(10)
second = Counter(100)
first.increase()
assert first.value == 11
assert second.value == 100  # Each object owns separate state.


# YOUR TURN
class Task:
    def __init__(self, title):
        # TODO: store title in self.title and False in self.complete.
        pass

    def mark_complete(self):
        # TODO: change this object's complete attribute to True.
        pass


learn = Task("Learn classes")
practice = Task("Practice methods")
assert hasattr(learn, "title"), "In __init__, write self.title = title"
assert hasattr(learn, "complete"), "In __init__, write self.complete = False"
assert learn.title == "Learn classes"
assert learn.complete is False
learn.mark_complete()
assert learn.complete is True
assert practice.complete is False
print("Lesson 04.10 passed: you created objects with state and behavior.")
