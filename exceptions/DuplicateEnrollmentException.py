class DuplicateEnrollmentException(Exception):
    def __init__(self, message="student is already enrolled in the course"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
