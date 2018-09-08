class CustomException(Exception):
    def __init__(self, *args, **kwargs):
        return super().__init__(self, *args, **kwargs)
    def __str__(self):
        return str(self.args [1])
class DeprecatedException(CustomException):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class DailyLimitException(CustomException):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class InvalidArgumentException(CustomException):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class KeyOrAuthEmptyException(CustomException):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class NotFoundException(CustomException):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class NotSupported(CustomException):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class SessionLimitException(CustomException):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class WrongCredentials(CustomException):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class PaladinsOnlyException(CustomException):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class SmiteOnlyException(CustomException):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class RealmRoyaleOnlyException(CustomException):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
