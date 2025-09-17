from dataclasses import dataclass
from enum import Enum

class AccessType(Enum):
    USER = 1
    USER_ADMIN = 2
    SYSTEM_ADMIN = 3


@dataclass
class User:
    name: str
    password: str
    access: AccessType

    def __hash__(self):
        thisHash = hash((self.name, self.password, self.access))
        return thisHash

    def __eq__(self, other):
        return isinstance(other, User) and self.name == other.name and self.password == other.password and other.access == self.access
