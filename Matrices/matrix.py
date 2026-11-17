import numpy as np
import sympy as sp



class Matrix:

    def __sigma_sum(self, mat1, mat2, i, j):
        val = 0
        for c in range(mat1.size('m')): # SOMETHING IS WRONG WITH THAT
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

    def __mul__(self, other):
        if (other).__class__.__name__ == "int": return Matrix([ [ self.value[i][j] * other for j in range(self.size('m'))] for i in range(self.size('n')) ])

        if self.size('m') != other.size('n'): return None

        return Matrix([ [ (self.__sigma_sum(self, other, i, j)) for j in range(other.size('m')) ] for i in range(self.size('n'))])
 
        pass

    def __rmul__(self, other):
        if (other).__class__.__name__ == "int": return Matrix([ [ self.value[i][j] * other for j in range(self.size('m'))] for i in range(self.size('n')) ])

        return None

    def __eq__(self, other):
        if (self).__class__.__name__ == "Matrix" and (other).__class__.__name__ == "Matrix":
            if self.size('n') != other.size('n') and self.size('m') != other.size('m') : return False

            for i in range(self.size('n')):
                for j in range(self.size('m')):
                    if self.value[i][j] != other.value[i][j] : return False

            return True

        return False

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


def transpode(mat: Matrix):
    if not (mat).__class__.__name__ == "Matrix": return None

    val = []
    for i in range(mat.size('m')):
        val.append([])
        for j in range(mat.size('n')):
            val[i].append(mat.value[j][i])

    return Matrix(val)



def adjoin(mat: Matrix):
    if not (mat).__class__.__name__ == "Matrix" : return None

    val = []
    for i in range(mat.size('n')):
        val.append([])
        for j in range(mat.size('m')):
            if mat.value[i][j].imag < 0 : val[i].append(mat.value[i][j].real + (-1) * mat.value[i][j].imag * 1j)
            else : val[i].append(mat.value[i][j])

    return Matrix(val)


def determinant(mat: Matrix):
    if (mat).__class__.__name__ == "Matrix": return None
    if not mat.is_quadratic(): return None

    # Elementary transformations

    

# A = Matrix([[2, 3, 0], [1, -2, 1]])
# B = Matrix([[1, -2], [2, 0], [-1, 1]])

# C = Matrix([[1,2],[3,4]])
# D = Matrix([[5,6],[7,8]])
# E = Matrix([[9,10],[-1,0]])
# IDENTITY_MATRIX = Matrix([[1, 0], [0, 1]])


# print(IDENTITY_MATRIX.is_identity())
# print( C * IDENTITY_MATRIX == C)
# print(C)
# print(C * IDENTITY_MATRIX)
# print( C * ( D + E ) == C * D + C * E)
# print( C * D != D * C)

A = Matrix([[2, 3, 3j], [1, -2, -2j]])
print(A)
print(transpode(A))
print(transpode(6))
print(adjoin(A))