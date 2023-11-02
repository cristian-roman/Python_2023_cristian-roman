class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]

    def get_element(self, i, j):
        return self.matrix[i][j]

    def set_element(self, i, j, value):
        self.matrix[i][j] = value

    def get_transpose(self):
        transpose = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transpose.set_element(j, i, self.get_element(i, j))
        return transpose

    def __str__(self):
        result = ""
        for i in range(self.n):
            for j in range(self.m):
                result += str(self.get_element(i, j)) + " "
            result += "\n"
        return result

    def multiply_by_matrix(self, m):
        return multiply_matrices(self, m)

    def iterate_with_transformation(self, func: callable([int])):

        temp = Matrix(self.n, self.m)

        for i in range(self.n):
            for j in range(self.m):
                temp.set_element(i, j, func(self.get_element(i, j)))

        return temp


def multiply_matrices(m1: Matrix, m2: Matrix) -> Matrix:
    if m1.m != m2.n:
        raise ValueError("Matrices cannot be multiplied")

    result = Matrix(m1.n, m2.m)

    for i in range(m1.n):
        for j in range(m2.m):
            result.set_element(i, j, 0)

    for i in range(m1.n):
        for j in range(m1.m):
            for k in range(m2.m):
                result.set_element(i, k, result.get_element(i, k) + m1.get_element(i, j) * m2.get_element(j, k))

    return result
