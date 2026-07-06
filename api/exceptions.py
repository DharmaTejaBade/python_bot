class DeltaAPIError(Exception):
    """Base API Exception"""
    pass


class AuthenticationError(DeltaAPIError):
    pass


class OrderError(DeltaAPIError):
    pass