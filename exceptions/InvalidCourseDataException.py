class InvalidCourseDataException(Exception):
    def __init__(self, message="invalid course data"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message