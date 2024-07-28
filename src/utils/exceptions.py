class InvalidEquationError(Exception):
    def __init__(self, message):
        super().__init__(self.message)
        self.message = message


class InitialValuesError(Exception):
    def __init__(self, message):
        super().__init__(self.message)
        self.message = message


class CalculationError(Exception):
    def __init__(self, message):
        super().__init__(self.message)
        self.message = message
