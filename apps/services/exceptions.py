class UploadFileException(Exception):


    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f'{type(self).__name__}: {self.message}'