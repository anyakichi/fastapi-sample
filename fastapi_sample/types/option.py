from dataclasses import dataclass
from typing import Callable, Generic, Optional, TypeVar

A = TypeVar("A")
B = TypeVar("B")


@dataclass
class Option(Generic[A]):
    value: A

    def unwrap(self) -> A:
        """
        >>> Option(10).unwrap()
        10
        >>> Option(None).unwrap()
        Traceback (most recent call last):
        ValueError
        """
        if self.value is None:
            raise ValueError
        return self.value

    def unwrap_or(self, default: A) -> A:
        """
        >>> Option(10).unwrap_or(20)
        10
        >>> Option(None).unwrap_or(20)
        20
        """
        if self.value is None:
            return default
        return self.value

    def map(self, f: Callable[[A], B]) -> Optional[B]:
        """
        >>> Option(4).map(lambda x: x * x)
        16
        >>> Option(None).map(lambda x: x * x)
        """
        if self.value is None:
            return None
        return f(self.value)

    def iter(self, f: Callable[[A], None]) -> None:
        """
        >>> Option(4).iter(lambda x: x * x)
        >>> Option(4).iter(lambda x: (_ for _ in ()).throw(Exception))
        Traceback (most recent call last):
        Exception
        >>> Option(None).iter(lambda x: (_ for _ in ()).throw(Exception))
        """
        self.map(f)
