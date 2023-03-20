class real(object):
    def __init__(self):
        self.re = float(0.0)
    
    def isLower(self, other) -> bool:
        if not isinstance(other, real):
            raise TypeError("other must be of type real")
        return self.re < other.re