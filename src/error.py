"""

"""

class GofileResponseError(Exception):
    """Exception raised for errors in the api response
    """

    def __init__(self, message="Unknown Response Error"):
        self.message = message
        super().__init__(self.message)