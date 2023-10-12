"""
make a simple program to multiply two randomized n x n matrices
"""
from random import randint

n = int(input())
matrix1 = [[randint(1,10) for i in range(n)] for i in range(n)]
matrix2 = [[randint(1,10) for i in range(n)] for i in range(n)]
matrixAns = [[0 for i in range(n)] for i in range(n)]

print("MATRIX 1")
for i in range(n):
    for j in range(n):
        print(matrix1[i][j],end=" ")
    print()

print("\nMATRIX 2")
for i in range(n):
    for j in range(n):
        print(matrix2[i][j],end=" ")
    print()

for i in range(n):
    for j in range(n):
        for k in range(n):
            matrixAns[i][j] += matrix1[i][k] * matrix2[k][j]

print("\nANSWER")
for i in range(n):
    for j in range(n):
        print(matrixAns[i][j],end=" ")
    print()

#complexity = O(n * n * n)
