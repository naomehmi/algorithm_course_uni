"""
convert a decimal number to binary
"""
def convert(n):
    if n >= 2:
        convert(n // 2)
    print(n % 2,end="")

n = int(input("Input a decimal number : "))

convert(n)

#complexity = O(log n)
