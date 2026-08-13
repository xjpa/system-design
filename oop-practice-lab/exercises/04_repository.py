"""Milestone 4: A repository abstraction.

Run: python exercises/04_repository.py

Implement InMemoryIssueRepository only. Everything else is supporting material.
Concepts: Protocol, abstraction, collection ownership, fake implementations.
"""

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID


@dataclass
class Issue:
    id: UUID
    title: str


class DuplicateIssueError(Exception):
    pass


class IssueNotFoundError(Exception):
    pass


class IssueRepository(Protocol):
    def add(self, issue: Issue) -> None: ...

    def get(self, issue_id: UUID) -> Issue | None: ...

    def update(self, issue: Issue) -> None: ...

    def list_all(self) -> list[Issue]: ...


class InMemoryIssueRepository:
    def __init__(self) -> None:
        # TODO: create a private dictionary keyed by UUID.
        raise NotImplementedError

    def add(self, issue: Issue) -> None:
        # TODO: reject a duplicate ID.
        raise NotImplementedError

    def get(self, issue_id: UUID) -> Issue | None:
        raise NotImplementedError

    def update(self, issue: Issue) -> None:
        # TODO: reject an unknown ID.
        raise NotImplementedError

    def list_all(self) -> list[Issue]:
        # TODO: return a new list, not the internal collection.
        raise NotImplementedError


def use_repository(repository: IssueRepository) -> int:
    """This function accepts any object matching the protocol."""
    return len(repository.list_all())


def expect_error(error_type: type[Exception], action: object) -> None:
    try:
        action()  # type: ignore[operator]
    except error_type:
        return
    raise AssertionError(f"Expected {error_type.__name__}")


def run_tests() -> None:
    repository = InMemoryIssueRepository()
    issue = Issue(UUID(int=1), "Cannot update profile")
    repository.add(issue)
    assert repository.get(issue.id) is issue
    assert use_repository(repository) == 1
    expect_error(DuplicateIssueError, lambda: repository.add(issue))
    expect_error(IssueNotFoundError, lambda: repository.update(Issue(UUID(int=2), "x")))

    result = repository.list_all()
    result.clear()
    assert len(repository.list_all()) == 1
    issue.title = "Updated title"
    repository.update(issue)
    assert repository.get(issue.id).title == "Updated title"  # type: ignore[union-attr]
    print("Milestone 4 passed: repository behavior is behind an interface.")


if __name__ == "__main__":
    run_tests()
