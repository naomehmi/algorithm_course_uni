"""
merge sort algorithm to sort an array of integers
"""
def mergeSort(arr,left,middle,right):
    L = arr[left:middle]
    R = arr[middle:right]
    i = 0
    j = 0
    k = left
    while i + left < middle and j + middle < right:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i + left < middle:
        arr[k] = L[i]
        i += 1
        k += 1
    while j + middle < right:
        arr[k] = R[j]
        j += 1
        k += 1

def divide(arr,left,right):
    if right - left > 1:
        middle = (left + right) // 2
        divide(arr,left,middle)
        divide(arr,middle,right)
        mergeSort(arr,left,middle,right)

arr = list(map(int,input().split()))

divide(arr,0,len(arr))

print("sorted array :",end=" ")
for i in arr:
    print(i,end=" ")
print()

#complexity : O(n log n)
