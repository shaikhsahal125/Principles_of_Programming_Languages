import sys

file = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

d1 = file.readline()
l1 = d1.split(" ")
l1 = [int(i) for i in l1]
m1 = l1[0]
n1 = l1[1]

matrix1 = [[0.0 for j in range(0, n1)] for i in range(0, m1)]

for i in range(0, m1):
    row = file.readline()
    num = row.split(" ")
    num = [float(i) for i in num]
    for j in range(0, n1):
        matrix1[i][j] = num[j]

d2 = file.readline()
l2 = d2.split(" ")
l2 = [int(i) for i in l2]
m2 = l2[0]
n2 = l2[1]


matrix2 = [[0.0 for j in range(0, n2)] for i in range(0, m2)]

for i in range(0, m2):
    row2 = file.readline()
    num2 = row2.split(" ")
    num2 = [float(i) for i in num2]
    for j in range(0, n2):
        matrix2[i][j] = num2[j]

# Matrix multiplication Algo:
matrix3 = [[0.0 for i in range(0, n2)] for j in range(0, m1)]
if n1 is m2:
    for i in range (0, m1):
        for j in range(0, n2):
            matrix3[i][j] = 0.0
            for k in range(0, n1):
                matrix3[i][j] = matrix1[i][k] * matrix2[k][j] + matrix3[i][j]
    # print the matrix
    for i in range(0, m1):
        for j in range(0, n2):
            print(matrix3[i][j], end = " ")
        print()
            
else:
    print('invalid input')
