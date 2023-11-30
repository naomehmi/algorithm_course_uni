"""
in an array of numbers between 0-9 inclusive separated by space, count the amount of 0s, 1s, 2s, ... , 9s in that array and print them each on one line

e.g. 3 8 2 0 4 5 6 9 1 7 3 3 1 2

output:
1
2
3
3
1
6
3
9
8
5

explanation : in the array, there are 1 number zero, 2 number ones, 3 number twos, 3 number threes, and so on.

"""

arr = list(map(int,input().split()))
amt = [0 for i in range(10)]

for i in range(len(arr)):
    amt[arr[i]] += 1

for i in range(10):
    print(amt[i])

#complexity = O(n)
