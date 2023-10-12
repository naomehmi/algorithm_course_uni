"""
In an array of 8 alphabetical coins (A-Z), there are 7 identical coins and 1 different coin. Find the position of the different coin. If all 8 coins are the same, output -1

e.g. YXXXXXXX
output = 1

e.g. BBBABBBB
output = 4

e.g. BBBBBBBB
output = -1
"""

coins = input()
identifier = coins[0]
ans = -1
for i in range(len(coins)):
    if identifier != coins[i]:
        if i == 1:
            if identifier == coins[2]:
                ans = 2
            else:
                ans = 1
            break
        else:
            ans = i + 1
print(ans)

# kinda hesitant whether this code implements brute force or not, it uses a linear search algorithm tho
# complexity = O(n)
