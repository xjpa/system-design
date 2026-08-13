"""FOUNDATIONS 13: Imports, enums, and dataclasses

Run: python foundations/13_imports_enums_dataclasses.py

An import brings in code that somebody already wrote:

    from dataclasses import dataclass

Read this as: "from the dataclasses module, import the name dataclass."

An Enum defines a small, fixed set of choices. This is safer than inconsistent
strings such as "open", "Open", and "OPEN":

    class Status(Enum):
        OPEN = auto()
        CLOSED = auto()

A dataclass generates repetitive class code such as __init__ for classes that
mainly hold data:

    @dataclass
    class User:
        name: str
        age: int

    user = User("Ada", 28)

The @dataclass decorator examines the annotated attributes and creates the
initializer. `frozen=True` prevents normal changes after construction.
"""

from dataclasses import FrozenInstanceError, dataclass
from enum import Enum, auto


# WORKED EXAMPLE
class Status(Enum):
    OPEN = auto()
    CLOSED = auto()


@dataclass(frozen=True)
class Ticket:
    title: str
    status: Status


ticket = Ticket("Export fails", Status.OPEN)
assert ticket.title == "Export fails"
assert ticket.status is Status.OPEN
try:
    ticket.title = "Changed"  # type: ignore[misc]
except FrozenInstanceError:
    pass
else:
    raise AssertionError("A frozen dataclass should reject changes")


# YOUR TURN
class Priority(Enum):
    # TODO: add LOW and HIGH choices, each assigned auto().
    pass


# TODO: put the dataclass decorator here and make it frozen.
class Task:
    title: str
    priority: Priority


assert hasattr(Priority, "LOW"), "Add LOW = auto() inside Priority"
assert hasattr(Priority, "HIGH"), "Add HIGH = auto() inside Priority"
task = Task("Study OOP", Priority.HIGH)
assert task.title == "Study OOP"
assert task.priority is Priority.HIGH
print("Foundations 13 passed: you used enums and generated class boilerplate.")
