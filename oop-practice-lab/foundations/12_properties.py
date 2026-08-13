"""FOUNDATIONS 12: Private attributes and properties

Run: python foundations/12_properties.py

By convention, an attribute beginning with _ is internal to the class:

    self._balance = 0

A property provides controlled read access:

    @property
    def balance(self):
        return self._balance

Callers then write account.balance, without parentheses. They cannot normally
assign account.balance because no setter was defined.

`@property` is a decorator: it changes how the method immediately below it is
used. For now, remember this practical rule:

- normal method: object.method()
- property: object.property_name

Properties are useful when you want object.attribute readability without
allowing callers to freely replace internal state.
"""


# WORKED EXAMPLE
class Score:
    def __init__(self, points: int) -> None:
        self._points = points

    @property
    def points(self) -> int:
        return self._points

    def add(self, amount: int) -> None:
        self._points = self._points + amount


score = Score(10)
assert score.points == 10
score.add(5)
assert score.points == 15


# YOUR TURN
class Temperature:
    def __init__(self, celsius: int) -> None:
        # TODO: store celsius in an internal _celsius attribute.
        pass

    # TODO: create a celsius property that returns self._celsius.


temperature = Temperature(25)
assert hasattr(temperature, "_celsius"), "Store celsius on self._celsius"
assert hasattr(Temperature, "celsius"), "Add @property and def celsius(self)"
assert temperature.celsius == 25
print("Foundations 12 passed: you can read controlled object state.")
