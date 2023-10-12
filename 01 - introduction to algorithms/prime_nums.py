"""
Determine how many prime numbers are in an array of integers
"""
import math
arr = list(map(int,input().split()))
totalPrimes = 0
for i in range(len(arr)):
    if arr[i] == 1:
        prime = False
    else:
        prime = True
    if arr[i] > 2:
        for j in range(2,arr[i]):
            if arr[i] % j == 0:
                prime = False
                break
    if prime:
        totalPrimes += 1
print(totalPrimes)

#complexity = O(n * n)
