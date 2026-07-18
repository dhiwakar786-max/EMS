"""Database engine & session factory (stub — no implementation)."""

from collections.abc import Generator

from sqlalchemy.orm import Session


def get_db() -> Generator[Session, None, None]:
    raise NotImplementedError
    yield  # pragma: no cover
