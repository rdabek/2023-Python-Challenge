from exercise1.real import real

class complex(real):
    def __init__(self):
        self.im = float(0.0)
        super().__init__()
    
    def isLower(self, other) -> bool:
        if not isinstance(other, complex):
            raise TypeError("other must be of type real")
        return real.isLower(self, other) and self.im < other.im