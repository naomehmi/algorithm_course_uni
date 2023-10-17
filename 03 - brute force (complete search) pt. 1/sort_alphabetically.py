"""
sort a string lexicographically (starting from uppercase letters and ignore whitespaces from input)

e.g. Hello World
output = H W d e l l l o o r 
"""

string = list(input().replace(" ",""))
nonBrute = string.copy()
brute = string.copy()

# BRUTE FORCE APPROACH (nested loop) (complexity = O(n * n))
for i in range(len(brute)):
    for j in range(len(brute)):
        if(ord(brute[i]) < ord(brute[j])):
            brute[i], brute[j] = brute[j], brute[i]
print("BRUTE FORCE APPROACH :",end=" ")
for i in range(len(brute)):
    print(brute[i],end=" ")
print()

# NON BRUTE FORCE APPROACH (sort with key) (complexity = O(n log n))
nonBrute.sort(key = lambda x : ord(x))

print("NON BRUTE FORCE APPROACH :",end=" ")
for i in range(len(nonBrute)):
    print(nonBrute[i],end=" ")
print()
