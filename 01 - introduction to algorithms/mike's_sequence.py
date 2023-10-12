"""
Help Mike make a sequence of numbers.

The sequence will start from the number S, and each number beside each other has a difference of D, and the sequence contains N numbers.
"""
n = int(input("How many numbers are in the sequence? "))
s = int(input("What number does the sequence start with? "))
d = int(input("What is the difference of the numbers beside each other in the sequence? "))

for i in range(n):
    print(s + i * d,end=" ")

# e.g. n = 7, s = 2, d = 5
# output -> 2 7 12 17 22 27 32

#complexity = O(n)
