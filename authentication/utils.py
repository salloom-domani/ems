from enum import Enum


class UserType(str, Enum):
    MANAGER = 'M'
    COMANAGER = 'C'
    EMPLOYEE = 'E'
