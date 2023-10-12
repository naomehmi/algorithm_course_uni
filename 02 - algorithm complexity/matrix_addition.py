"""
A simple program to calculate the addition of two randomized n x n matrices
"""
from random import randint
n = int(input("Size of matrices : "))
matrix1 = [[randint(1,10) for i in range(n)] for i in range(n)]
matrix2 = [[randint(1,10) for i in range(n)] for i in range(n)]
total = matrix1.copy()

for i in range(n):
    for j in range(n):
        total[i][j] += matrix2[i][j]

for i in range(n):
    for j in range(n):
        print(total[i][j],end=" ")
    print()

#complexity = O(n * n)
