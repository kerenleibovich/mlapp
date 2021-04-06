from mlapp.utils.exceptions.base_exceptions import UserException


class MissingModelException(UserException):
    pass

class MissingArgumentsError(UserException):
    pass
