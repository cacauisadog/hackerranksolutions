def flippingMatrix(matrix):
    n = len(matrix[0]) // 2
    size = len(matrix[0]) - 1
    max_sum = 0

    for i in range(n):
        for j in range(n):
            max_sum += max(matrix[i][j], matrix[i][size - j], matrix[size - i][j], matrix[size - i][size - j])

    return max_sum


print(flippingMatrix([[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]))

# [112, 42, 83, 119]
# [56, 125, 56, 49]
# [15, 78, 101, 43]
# [62, 98, 114, 108]
