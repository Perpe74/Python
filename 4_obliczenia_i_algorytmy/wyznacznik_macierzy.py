import random
import numpy as np

random.seed()
matrix = []
det = 0

for i in range(0,3):
    matrix.append([])
    for j in range(0,3):
           matrix[i].append(random.randint(-10,10))

det = np.linalg.det(matrix)

print(matrix)
print(det)