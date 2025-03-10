#!/usr/bin/env python

#matrix multiplication using lists

matrix_a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

for i in range(4):
    for j in range(3):
        print(matrix_a[i],[j])



print(matrix_a[0][0])
print(matrix_a[0][2])
print(matrix_a[2][0])


matrix_a = [[1, 2],
            [3, 4]]
            
matrix_b = [[5, 6]
            [7, 8]]           

result = [[0, 0]
          [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = (matrix_a[i][0] * matrix_b[0][j] +
                        matrix_a[i][1] * matrix_b[1][j])

for row in result:
    print(row)



    