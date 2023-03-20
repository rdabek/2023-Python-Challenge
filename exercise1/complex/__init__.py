from exercise1.real import real

class complex(real):
    def __init__(self):
        real.__init__()
        self.im = float(0.0)
    
    def isLower(self, other) -> bool:
        if not isinstance(other, real):
            raise TypeError("other must be of type real")
        return real.isLower(other) and self.im < other.im