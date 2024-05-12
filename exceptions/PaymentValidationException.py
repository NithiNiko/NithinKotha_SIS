
class PaymentValidationException(Exception):
    def __init__(self, message="error in payment validation"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message