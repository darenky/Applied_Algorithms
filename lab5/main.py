from matrix import Matrix
from vector import Vector
from lup import LinearSystemSolver

if __name__ == "__main__":
    A = Matrix([
        [4, -1, 0, -2, 0, 0],
        [-1, 4, -1, 0, -2, 0],
        [0, -1, 4, 0, 0, -2],
        [-2, 0, 0, 4, -1, 0],
        [0, -2, 0, -1, 4, -1],
        [0, 0, -2, 0, -1, 4]
    ])
    
    b = Vector([1, 5, 0, 2, 4, 1])
    solver = LinearSystemSolver()
    solution = solver.solve(A, b)
    print("Solution:", solution.data)

    result = A * solution
    print("\nVerification (A * x):", result.data)
    print("Original b:", b.data)