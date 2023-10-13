"""
a simple program program to calculate M power of N (N ^ M) using divide and conquer algo

explanation: https://youtu.be/7HtsNw8NWSo?si=MIqXUi5ELlwQhRsf
"""
def power(n,m):
    if m == 0:
        return 1
    elif m % 2 == 1:
        return n * power(n,m-1)
    elif m % 2 == 0:
        return power(n, m//2) * power(n,m//2)
n, m = list(map(int,input().split()))
print(power(n,m))

#complexity = O(log n)
