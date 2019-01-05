class BotError(Exception):
    def __init__(self, msg, function_name, result):
        super(BotError, self).__init__("A request to the Telegram API was unsuccessful. {0}".format(msg))
        self.function_name = function_name
        self.result = result
