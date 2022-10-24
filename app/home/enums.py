from enum import Enum


class Size(Enum):
    DEFAULT = 'Select a header size'
    H2 = 'H2'
    H3 = 'H3'
    H4 = 'H4'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value
