# Class PSNAWPException
# Used to generate custom exceptions for the API
# For internal use only do not call directly

class PSNAWPException(Exception):
    """
    Generic Exception
    """

    def __init__(self, message):
        super().__init__(message)


class PSNAWPIllegalArgumentError(Exception):
    """
    Exception raised if user gave wrong input to a function
    """

    def __init__(self, message):
        super().__init__(message)


class PSNAWPUserNotFound(Exception):
    """
    Exception raised if user request was invalid
    """

    def __init__(self, message):
        super().__init__(message)


class PSNAWPAuthenticationError(Exception):
    """
    Exception for authentication related errors
    """

    def __init__(self, message):
        super().__init__(message)
