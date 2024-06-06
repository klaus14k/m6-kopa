class NegativeTitlesError (Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message

class InvalidYearCupError (Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message

class ImpossibleTitlesError (Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
