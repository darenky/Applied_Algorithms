from vector import Vector

class Matrix:

    def __init__(self, data):
        self.data = self._convert_to_list_of_lists(data)
        self.rows = len(self.data)
        self.cols = len(self.data[0])
        
        if self.rows != self.cols:
            raise ValueError("Matrix must be square")
    
    @staticmethod
    def _convert_to_list_of_lists(data):
        if isinstance(data, list) and all(isinstance(row, list) for row in data):
            return [[float(elem) for elem in row] for row in data]
        else:
            raise ValueError("Input data must be a list of lists")
    
    def __str__(self):
        return str(self.data)
    
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match")
        return Matrix([[a + b for a, b in zip(self.data[i], other.data[i])] for i in range(self.rows)])
    
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match")
        return Matrix([[a - b for a, b in zip(self.data[i], other.data[i])] for i in range(self.rows)])
    
    def __mul__(self, other):

        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Matrix dimensions must match")
            result = [[sum(a * b for a, b in zip(self.data[i], col)) for col in zip(*other.data)] for i in range(self.rows)]
            return Matrix(result)
        
        elif isinstance(other, Vector):
            if self.cols != other.size:
                raise ValueError("Matrix and vector dimensions must match")
            result = [sum(a * b for a, b in zip(self.data[i], other.data)) for i in range(self.rows)]
            return Vector(result)
        
        else:
            raise TypeError("Multiplication is only supported between matrices and vectors")
    
    def get_size(self):
        return self.rows, self.cols