import pprint

def matrix_multiple(mat1, mat2):
    new_matrix = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                new_matrix[i][j] += mat1[i][k] * mat2[k][j]
                new_matrix[i][j] %= 1000000007

    return new_matrix

def matrix_square(matrix, n):

    if n == 1:
        return matrix
    
    if n%2 == 0:
        square_matrix = matrix_square(matrix, n//2)
        return matrix_multiple(square_matrix, square_matrix)
    
    else:
        square_matrix = matrix_square(matrix, n//2)
        return matrix_multiple(matrix_multiple(square_matrix, square_matrix), matrix)

def main():
    campus = [[0] * 8 for _ in range(8)]
    campus[0][1] = campus[0][2] = 1
    campus[1][0] = campus[1][2] = campus[1][3] = 1
    campus[2][0] = campus[2][1] = campus[2][3] = campus[2][4] = 1
    campus[3][1] = campus[3][2] = campus[3][4] = campus[3][5] = 1
    campus[4][2] = campus[4][3] = campus[4][5] = campus[4][7] = 1
    campus[5][3] = campus[5][4] = campus[5][6] = 1
    campus[6][5] = campus[6][7] = 1
    campus[7][4] = campus[7][6] = 1
    n = int(input())

    campus = matrix_square(campus, n)

    print(campus[0][0])

main()