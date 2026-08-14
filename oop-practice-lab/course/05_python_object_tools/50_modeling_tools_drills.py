"""LESSON 05.50: Python object-modeling tool drills.

Run: python course/05_python_object_tools/50_modeling_tools_drills.py

The goal is not to use every Python feature. Choose a tool because it expresses
a modeling decision: enum for vocabulary, dataclass for data, property for
controlled access, and classmethod for an alternate construction path.
"""

from dataclasses import dataclass
from enum import Enum, auto


# WORKED EXAMPLE — a frozen dataclass models one immutable descriptive value
@dataclass(frozen=True)
class Size:
    width: int
    height: int


assert Size(4, 3) == Size(4, 3)


# DRILL 1 — enum: restrict a value to named choices
class Priority(Enum):
    # TODO: define LOW, NORMAL, and HIGH with auto().
    pass


# These checks intentionally fail until all three members exist.
assert Priority.LOW is not Priority.HIGH
assert len(Priority) == 3


# DRILL 2 — frozen dataclass: immutable descriptive value
@dataclass(frozen=True)
class Coordinate:
    # TODO: declare integer fields named x and y.
    pass


origin = Coordinate(0, 0)
assert origin == Coordinate(0, 0)
assert origin != Coordinate(1, 0)


# DRILL 3 — property: calculate a read-only public value
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    @property
    def area(self) -> float:
        # TODO: return width multiplied by height.
        raise NotImplementedError


assert Rectangle(4, 3).area == 12


# DRILL 4 — classmethod: name an alternate way to construct an object
@dataclass(frozen=True)
class EmailAddress:
    value: str

    @classmethod
    def from_text(cls, raw: str) -> "EmailAddress":
        # TODO: strip and lowercase raw, reject blank text, then return cls(...).
        raise NotImplementedError


assert EmailAddress.from_text(" ADA@EXAMPLE.COM ") == EmailAddress("ada@example.com")


# DRILL 5 — equality by identity for an entity
class User:
    def __init__(self, user_id: int, name: str) -> None:
        self.id = user_id
        self.name = name

    def __eq__(self, other: object) -> bool:
        # TODO: return NotImplemented if other is not a User.
        # TODO: otherwise compare IDs, not names.
        return False


assert User(1, "Ada") == User(1, "A. Lovelace")
assert User(1, "Ada") != User(2, "Ada")
assert (User(1, "Ada") == "Ada") is False


# TRANSFER CHALLENGE — combine enum, dataclass, normalization, and a property
class Unit(Enum):
    CELSIUS = auto()
    FAHRENHEIT = auto()


@dataclass(frozen=True)
class Temperature:
    value: float
    unit: Unit

    @property
    def celsius(self) -> float:
        # TODO: return value unchanged for Celsius; convert Fahrenheit otherwise.
        # Formula: (value - 32) * 5 / 9
        raise NotImplementedError


assert Temperature(20, Unit.CELSIUS).celsius == 20
assert Temperature(68, Unit.FAHRENHEIT).celsius == 20

print("Lesson 05.50 passed: modeling choices are explicit in the code.")
