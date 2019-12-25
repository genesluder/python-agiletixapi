class AgileException(Exception):

    def __init__(self, code=None, message=None, *args, **kwargs):
        self.code = code
        self.message = message
        super(AgileException, self).__init__(*args, **kwargs)


class InternalException(AgileException):
    pass


class ImproperlyConfigured(AgileException):
    pass


class AgileAPIException(AgileException):
    """All Agile API exceptions inherit from this exception.
    
    """
    pass


class NotFoundException(AgileAPIException):
    """The resource was not found

    """
    pass


class ClientError(AgileAPIException):
    """Client error

    """
    pass


class InvalidPromoException(AgileAPIException):
    """The promo enterd was invalid.

    """
    pass


class InternalServerError(AgileAPIException):
    """Internal server error

    """
    pass


class ServiceUnavailable(AgileAPIException):
    """The service is unavailable.

    """
    pass
