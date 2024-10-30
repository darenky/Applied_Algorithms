
class Vector:
    
    def __init__(self, data):
        self.data = [float(x) for x in data]
        self.size = len(self.data)
    
    def __add__(self, other):
        if self.size != other.size:
            raise ValueError("Vector dimensions must match")
        return Vector([a + b for a, b in zip(self.data, other.data)])
    
    def __sub__(self, other):
        if self.size != other.size:
            raise ValueError("Vector dimensions must match")
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __str__(self):
        return str(self.data)