from matrix import Matrix
from vector import Vector
from copy import deepcopy

class LUPDecomposition:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = matrix.rows
        self.L = None # Lower triangular matrix
        self.U = None # Upper triangular matrix
        self.P = None # Permutation matrix
        self.decompose()
    
    def decompose(self):
        A = deepcopy(self.matrix.data)
        n = self.n
        pi = list(range(n))  
        
        for k in range(n):
            k_max = k 
            for i in range(k, n):
                if abs(A[i][k]) > abs(A[k_max][k]):
                    k_max = i
            
            if A[k_max][k] == 0:
                raise ValueError("Matrix is singular")
            
            A[k], A[k_max] = A[k_max], A[k]
            pi[k], pi[k_max] = pi[k_max], pi[k]
            
            for i in range(k + 1, n):
                A[i][k] = A[i][k] / A[k][k]
                for j in range(k + 1, n):
                    A[i][j] = A[i][j] - A[i][k] * A[k][j]
        
        L = [[1 if i == j else 0 if i < j else A[i][j] 
              for j in range(n)] for i in range(n)]
        
        U = [[0 if i > j else A[i][j] 
              for j in range(n)] for i in range(n)]
        
        P = [[1 if j == pi[i] else 0 
              for j in range(n)] for i in range(n)]
        
        self.L = Matrix(L)
        self.U = Matrix(U)
        self.P = Matrix(P)


class LinearSystemSolver:

    @staticmethod
    def solve(A, b):
        try:
            lup = LUPDecomposition(A)
        except ValueError as e:
            print(f"Error during decomposition: {e}")
            return None
        
        # Ly = Pb
        Pb = lup.P * b
        y = Vector([0.0] * b.size)
        
        # Forward substitution
        for i in range(b.size):
            sum_val = 0
            for j in range(i):
                sum_val += lup.L.data[i][j] * y.data[j]
            y.data[i] = Pb.data[i] - sum_val
        
        # Backward substitution
        x = Vector([0.0] * b.size)
        
        for i in range(b.size - 1, -1, -1):
            sum_val = 0
            for j in range(i + 1, b.size):
                sum_val += lup.U.data[i][j] * x.data[j]
            if abs(lup.U.data[i][i]) < 1e-10:
                raise ValueError(f"Zero encountered in diagonal of U at position {i}")
            x.data[i] = (y.data[i] - sum_val) / lup.U.data[i][i]
        
        return x