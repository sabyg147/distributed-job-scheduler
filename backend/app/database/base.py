from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all database models.

    Every ORM model in the project
    inherits from this class.
    """

    pass