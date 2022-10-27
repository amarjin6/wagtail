from enum import Enum


class Gender(Enum):
    DEFAULT = 'Choose a gender'
    MALE = 'male'
    FEMALE = 'female'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value


class Role(Enum):
    DEFAULT = 'Select role'
    VISITOR = 'visitor'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value


class Status(Enum):
    DEFAULT = 'Select status'
    PLANNING = 'planning'
    PROCESSING = 'processing'
    FINISHED = 'finished'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value


class Palette(Enum):
    RED = '#FF0000'
    BLUE = '#0000FF'
    GREEN = '#00FF00'
    BLACK = '#000000'
    GREY = '#808080'

    @classmethod
    def choices(cls):
        return [(attr.value, attr.name) for attr in cls]

    def __str__(self):
        return self.value
