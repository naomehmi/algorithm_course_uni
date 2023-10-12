"""
Check whether a substring M is found in string N

e.g. M = NOT, N = NOBODY NOTICED HIM

output = found

e.g. M = ALE, N = I'M AN ALIEN

output = not found
"""

m = input().upper()
n = input().upper()
found = False
for i in range(len(n)):
    if n[i] == m[0]:
        found = True
        for j in range(len(m)):
            if n[i+j] != m[j]:
                found = False
                break
    if found:
        break

if found:
    print("found")
else:
    print("not found")
            
#complexity = O(m * n)
