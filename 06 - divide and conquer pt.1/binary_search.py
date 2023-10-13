"""
determine the position of an element in a sorted array of integers using binary search

e.g. arr = 32 54 89 99 111 123 344 489
n = 111
output : 5

e.g. arr = 32 54 89 99 111 123 344 489
n = 600
output : not found
"""

def binarySearch(left, right):
    global arr, n
    if left < right:
        middle = (left + right) // 2
        if arr[middle] == n:
            return middle + 1
        elif arr[middle] > n:
            return binarySearch(left,middle)
        else:
            return binarySearch(middle+1,right)
    else:
        return "not found"

arr = list(map(int,input().split()))
n = int(input())
print(binarySearch(0,len(arr)))

#complexity = O(log n)
