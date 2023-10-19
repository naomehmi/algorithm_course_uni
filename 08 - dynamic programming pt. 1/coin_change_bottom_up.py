"""
simple program to find the minimum amount of coins needed that add up to N

e.g. arr = [1,2,5,6], N = 10
output: 2
explanation : 5 + 5 = 10, 2 coins needed

detailed explanation: https://youtu.be/H9bfqozjoqs?si=pKzMV9d-OzJdTScA 
"""

arr = list(map(int,input().split()))
n = int(input())

dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(n+1):
    for j in arr:
        print(dp)
        dp[i] = min(dp[i], 1 + dp[i - j])

print(dp[n])
