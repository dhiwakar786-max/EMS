"""Domain exceptions (stub)."""


class DomainError(Exception):
    """Base domain error."""


class EmployeeNotFoundError(DomainError):
    pass


class DepartmentNotFoundError(DomainError):
    pass
