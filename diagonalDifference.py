# https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/problem


def diagonalDifference(arr):
    size = len(arr)
    ltr_diagonal = _calculate_diagonal("ltr", arr, size)
    rtl_diagonal = _calculate_diagonal("rtl", arr, size)

    return abs(ltr_diagonal - rtl_diagonal)


def _calculate_diagonal(orientation, matrix, size):
    diagonal = []

    if orientation == "ltr":
        for i in range(size):
            diagonal.append(matrix[i][i])

    else:
        for i, j in zip(range(size), range(size - 1, -1, -1)):
            diagonal.append(matrix[i][j])

    return sum(diagonal)


print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
