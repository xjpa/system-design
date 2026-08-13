"""Milestone 2: A behavior-rich entity.

Run: python exercises/02_issue_entity.py

Everything required for this exercise is in this file. Implement Issue only.
Concepts: encapsulation, properties, class methods, invariants, state machines.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum, auto
from uuid import UUID


class Role(Enum):
    CUSTOMER = auto()
    AGENT = auto()


class Priority(Enum):
    NORMAL = auto()
    HIGH = auto()


class IssueStatus(Enum):
    OPEN = auto()
    IN_PROGRESS = auto()
    RESOLVED = auto()


class DomainError(Exception):
    pass


class InvalidTransitionError(DomainError):
    pass


class PermissionDeniedError(DomainError):
    pass


@dataclass(frozen=True, slots=True)
class User:
    id: UUID
    name: str
    role: Role


@dataclass(frozen=True, slots=True)
class Comment:
    author: User
    body: str
    created_at: datetime


class Issue:
    def __init__(
        self,
        *,
        issue_id: UUID,
        title: str,
        reporter: User,
        priority: Priority,
        opened_at: datetime,
    ) -> None:
        # TODO: validate and store fields; initial state is OPEN with no assignee.
        raise NotImplementedError

    @classmethod
    def open(
        cls,
        *,
        title: str,
        reporter: User,
        priority: Priority,
        opened_at: datetime,
        id_factory: Callable[[], UUID],
    ) -> Issue:
        # TODO: use the factory, then construct and return an Issue.
        raise NotImplementedError

    @property
    def id(self) -> UUID:
        raise NotImplementedError

    @property
    def status(self) -> IssueStatus:
        raise NotImplementedError

    @property
    def assignee(self) -> User | None:
        raise NotImplementedError

    @property
    def comments(self) -> tuple[Comment, ...]:
        # TODO: do not expose the mutable internal list.
        raise NotImplementedError

    def claim(self, agent: User) -> None:
        # TODO: only an AGENT can claim an OPEN issue.
        raise NotImplementedError

    def add_comment(self, *, author: User, body: str, created_at: datetime) -> None:
        # TODO: reject a blank body, then add an immutable Comment.
        raise NotImplementedError

    def resolve(self) -> None:
        # TODO: require IN_PROGRESS state, an assignee, and at least one comment.
        raise NotImplementedError

    def reopen(self) -> None:
        # TODO: only RESOLVED can become OPEN. Clear the old assignee.
        raise NotImplementedError


def expect_error(error_type: type[Exception], action: object) -> None:
    try:
        action()  # type: ignore[operator]
    except error_type:
        return
    raise AssertionError(f"Expected {error_type.__name__}")


def run_tests() -> None:
    customer = User(UUID(int=1), "Ada", Role.CUSTOMER)
    agent = User(UUID(int=2), "Lin", Role.AGENT)
    now = datetime(2026, 1, 15, tzinfo=timezone.utc)
    issue = Issue.open(
        title="Export fails",
        reporter=customer,
        priority=Priority.HIGH,
        opened_at=now,
        id_factory=lambda: UUID(int=100),
    )
    assert issue.id == UUID(int=100)
    assert issue.status is IssueStatus.OPEN
    assert issue.assignee is None
    assert issue.comments == ()
    expect_error(PermissionDeniedError, lambda: issue.claim(customer))
    expect_error(InvalidTransitionError, issue.resolve)

    issue.claim(agent)
    assert issue.status is IssueStatus.IN_PROGRESS
    expect_error(InvalidTransitionError, issue.resolve)
    issue.add_comment(author=agent, body="Fixed in build 42", created_at=now)
    assert isinstance(issue.comments, tuple) and len(issue.comments) == 1
    issue.resolve()
    assert issue.status is IssueStatus.RESOLVED
    issue.reopen()
    assert issue.status is IssueStatus.OPEN and issue.assignee is None
    expect_error(InvalidTransitionError, issue.reopen)
    print("Milestone 2 passed: Issue enforces its lifecycle.")


if __name__ == "__main__":
    run_tests()
