class Error(Exception):
    pass


class BotError(Error):
    def __init__(self, expression, message):
        self.exp = expression
        self.message = message
