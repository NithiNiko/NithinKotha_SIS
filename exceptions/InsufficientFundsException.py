class InsufficientFundsException(Exception):
    def __init__(self, message="insufficent funds for operation"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message