"""LESSON 06.20: Value objects.

Run: python course/06_oop_fundamentals/20_value_objects.py

Implement User and Comment until this file prints its success message.
Concepts: dataclass, enums, validation, normalization, immutability, equality.
"""

from dataclasses import FrozenInstanceError, dataclass
from datetime import datetime, timezone
from enum import Enum, auto
from uuid import UUID, uuid4


class Role(Enum):
    CUSTOMER = auto()
    AGENT = auto()


@dataclass(frozen=True, slots=True, eq=False)
class User:
    id: UUID
    name: str
    email: str
    role: Role

    def __post_init__(self) -> None:
        # TODO: reject a blank name and normalize the email.
        # Hint: a frozen dataclass requires object.__setattr__(self, "email", value).
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        # TODO: Users are equal when their IDs are equal.
        raise NotImplementedError

    def __hash__(self) -> int:
        # TODO: Objects that compare equal must have the same hash.
        raise NotImplementedError


@dataclass(frozen=True, slots=True)
class Comment:
    author: User
    body: str
    created_at: datetime

    def __post_init__(self) -> None:
        # TODO: reject a blank body and a timestamp without a timezone.
        raise NotImplementedError


def expect_error(error_type: type[Exception], action: object) -> None:
    try:
        action()  # type: ignore[operator]
    except error_type:
        return
    raise AssertionError(f"Expected {error_type.__name__}")


def run_tests() -> None:
    user_id = uuid4()
    user = User(user_id, "Ada", " ADA@Example.COM ", Role.CUSTOMER)
    assert user.email == "ada@example.com"
    assert user == User(user_id, "New Name", "new@example.com", Role.AGENT)
    assert user != User(uuid4(), "Ada", "ada@example.com", Role.CUSTOMER)
    expect_error(ValueError, lambda: User(uuid4(), " ", "a@b.com", Role.CUSTOMER))

    comment = Comment(user, "I can reproduce this", datetime.now(timezone.utc))
    try:
        comment.body = "changed"  # type: ignore[misc]
    except FrozenInstanceError:
        pass
    else:
        raise AssertionError("Comment should be immutable")
    expect_error(ValueError, lambda: Comment(user, " ", datetime.now(timezone.utc)))
    expect_error(ValueError, lambda: Comment(user, "body", datetime(2026, 1, 1)))
    print("Lesson 06.20 passed: valid, immutable value objects created.")


if __name__ == "__main__":
    run_tests()
