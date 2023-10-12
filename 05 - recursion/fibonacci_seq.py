"""
output the first n numbers of the fibonacci sequence
"""
def fibo(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input())

for i in range(n):
    print(fibo(i),end=" ")
print()

#complexity = O(2 ^ n)
