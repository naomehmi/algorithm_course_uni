"""
given an array of numbers, how many combinations can be made that add up to N

e.g. arr = 2 3 5 7, n = 7
output:
2 2 3
2 5
7

e.g. arr = 100 200 350, n = 800
output: 
100 100 100 100 100 100 100 100
100 100 100 100 100 100 200
100 100 100 100 200 200
100 100 200 200 200
100 350 350
200 200 200 200
"""
def comb(res,cur):
    global n,arr
    if sum(res) == n:
        for i in res:
            print(i,end=" ")
        print()
    if sum(res) < n:
        for i in range(cur,len(arr)):
            comb(res + [arr[i]],i)

arr = list(map(int,input().split()))
n = int(input())

comb([],0)

# complexity = O(2 ^ n)
