import numpy as np
import sympy as sp



class Matrix:

    # __SIGMA_SUM WORKS WRONG

    def __sigma_sum(self, mat1, mat2, i, j):
        val = 0
        for c in range(mat1.size('n')):
            val += mat1.value[i][c] * mat2.value[c][j]
        return val

    def __init__(self, mat):
        self.n = len(mat)
        self.m = len(mat[0])
        self.value = mat

    # magic method must be improved

    def __str__(self):
        expression = f"Matrix : [\n"
        for i in self.value:
            expression += str(i)
            expression += "\n"
        expression += "]"
        return expression

    def __call__(self):
        return self.value

    def __add__(self, other):
        if self.size('n') != other.size('n') and self.size('m') != other.size('m') : return None
        
        return Matrix([ [ self.value[i][j] + other.value[i][j] for j in range(self.size('m'))] for i in range(self.size('n')) ])

    # MULTIPLICATION NOT WORKING PROPERLY

    def __mul__(self, other):
        if (other).__class__.__name__ == "int": return Matrix([ [ self.value[i][j] * other for j in range(self.size('m'))] for i in range(self.size('n')) ])

        if self.size('m') != other.size('n'): return None

        return Matrix([ [ (self.__sigma_sum(self, other, i, j)) for j in range(other.size('m')) ] for i in range(self.size('n'))])
 
        pass

    def is_quadratic(self):
        return True if self.n == self.m else False

    def is_zero(self):
        for i in self.value:
            for j in i:
                if j != 0 : return False

        return True

    def is_diagonal(self):
        if not self.is_quadratic(): return False

        for i in range(self.n):
            for j in range(self.m):
                if ( i == j and ( self.value[i][j] == 0 ) ) or ( i != j and ( not self.value[i][j] == 0)):
                    return False

        return True

    def is_identity(self):
            if not self.is_quadratic(): return False
    
            for i in range(self.n):
                for j in range(self.m):
                    if ( i == j and ( not self.value[i][j] == 1 ) ) or ( i != j and ( not self.value[i][j] == 0 )):
                        return False
    
            return True

    def size(self, dim):
        if dim == 'n' : return self.n
        if dim == 'm' : return self.m
        return None

        # Think about using "__len__"


def add_matrices(M1: Matrix, M2: Matrix):
    if M1.size('n') != M2.size('n') and M1.size('m') != M2.size('m') : return None

    return Matrix([ [ M1.value[i][j] + M2.value[i][j] for j in range(M1.size('m'))] for i in range(M1.size('n')) ])


# potential_matrix = [
#     [1, 0, 0],
#     [0, 1, 1],
#     [0, 0, 0]
# ]

# matr = Matrix(potential_matrix)
# # print(f"{matr.size()[0]} * {matr.size()[1]}")
# # print(matr.is_quadratic())
# # print(matr.is_zero())
# # print(matr.is_diagonal())
# # print(matr.value)
# # print(matr())
# # print(matr)

# # print(matr.is_identity())

# print(matr)

a = [
    [2, 3, 1],
    [-1, 0, 2]
]
A = Matrix(a)

b = [
    [5, 5, 4],
    [1, -1, 0]
]
B = Matrix(b)

c = [
    [5, 0],
    [2, 1],
    [-3, -1]
]
C = Matrix(c)

print(A + B)
print(A * C)

# def sigma_sum(n_list, m_list):
#         val = 0
#         for c in range(len(n_list)):
#             val += n_list[c] * m_list[c]
#         return val

# print(sigma_sum([2, 3, 1], [5, 2, -3]))


# print(True if (7).__class__.__name__ == "int" else False) 
