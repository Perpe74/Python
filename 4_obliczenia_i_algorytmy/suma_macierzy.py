import random

random.seed()
matrix1 = []
matrix2 = []
matrix_sum=[]
max = 100

for i in range(0,128):
    matrix1.append([])
    matrix2.append([])
    for j in range(0,128):
           matrix1[i].append(random.random()*max)
           matrix2[i].append(random.random()*max)

for i in range(0,128):
    matrix_sum.append([])
    for j in range(0,128):
        matrix_sum[i].append(matrix1[i][j] + matrix2[i][j])

print(matrix1)
print(matrix2)
print(matrix_sum)
