class NegativeAgeException(RuntimeError):
    def __init__(self, age):
        self.age = age


