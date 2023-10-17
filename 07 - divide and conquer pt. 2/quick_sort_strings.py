"""
quick sort algorithm to sort an array of strings.

This code will sort the array based on the length of each string in ascending order, and if there are strings with the same length, it will be sorted lexicographically.

e.g. arr = angela, budi, didi, man, andri, sani
output : man, budi, didi, sani, andri, angela 

explanation : https://youtu.be/Hoixgm4-P4M?si=O5gT_fsJ8XAQyc1s (original code is in the pinned comment of this video)
"""
def partition(arr, left, right):
    pivotElement = (left + right) // 2
    pivot = arr[pivotElement]

    arr[pivotElement], arr[right] = arr[right], arr[pivotElement]
    
    p = left
    q = right-1

    while p <= q:
        if len(arr[p]) < len(pivot):
            p += 1
        elif len(arr[q]) > len(pivot):
            q -= 1
        elif len(arr[p]) == len(pivot) and arr[p] <= pivot:
            p += 1
        elif len(arr[q]) == len(pivot) and arr[q] >= pivot:
            q -= 1
        else:
            arr[p], arr[q] = arr[q], arr[p]
            p += 1
            q -= 1
    arr[p], arr[right] = arr[right], arr[p]
    return p

def quickSort(arr, left, right):
    if left < right:
        part = partition(arr, left, right)
        quickSort(arr, left, part - 1)
        quickSort(arr, part + 1, right)

arr = input().split()
quickSort(arr, 0, len(arr)-1)

print("sorted array :",end=" ")
for i in arr:
    print(i,end=" ")
print()

#complexity = O(n log n)
