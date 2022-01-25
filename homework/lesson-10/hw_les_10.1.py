class Matrix:
    def __init__(self, *matrix_list):
        self.matrix_list = list(matrix_list)

    def __str__(self):
        matrix = []
        for el in self.matrix_list:
            el = ['%4d\t' % i for i in el]
            lines = ''.join(el)
            matrix.append(lines)
        matrix = [str(el) for el in matrix]
        matrix = '\n'.join(matrix)
        return matrix

    def __add__(self, other):
        if len(self.matrix_list) != len(other.matrix_list):
            raise 'Матрицы разного размера'
        for i in range(0, len(self.matrix_list)):
            if len(self.matrix_list[i]) != len(other.matrix_list[i]):
                raise 'Матрицы разного размера'
        sum_matrix = []
        for i in range(0, len(self.matrix_list)):
            sum_el = []
            sum_matrix.append(sum_el)
            for j in range(0, len(self.matrix_list[i])):
                sum_el.append((self.matrix_list[i][j]) + (other.matrix_list[i][j]))
        return Matrix(*(el for el in sum_matrix))


m1 = Matrix([1, 2, 3], [4, 5, 5], [7, 8, 6])
m2 = Matrix([2, 5, 3], [5, 8, 3], [4, 7, 2])
print(m1 + m2)
