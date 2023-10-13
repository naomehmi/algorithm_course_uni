"""
a simple program to solve the tower of hanoi problem

in toh, there are basically three poles (A, B, and C). There are N stacks of disk in pole A, with the biggest disk at the bottom, up to the smallest disk at the top. The goal is to move all those stacks from A to C. Each time you try to move a disk to another pole, it is not allowed to stack disks where the disk on top is bigger than the disk on the bottom.

detailed explanation: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

this code is referenced from my class's module
"""

def toh(currentDisk, fromThisPole, toThisPole, theOtherPole):
    if currentDisk == 0:
        return
    toh(currentDisk-1,fromThisPole, theOtherPole, toThisPole)
    print(F"Moved disk {currentDisk} from pole {fromThisPole} to pole {toThisPole}")
    toh(currentDisk-1, theOtherPole, toThisPole, fromThisPole)

n = int(input("Amount of disks to move : "))

toh(n,"A","C","B")

#complexity = O(2 ^ n) -> cuz there are two possibilities for each disk
