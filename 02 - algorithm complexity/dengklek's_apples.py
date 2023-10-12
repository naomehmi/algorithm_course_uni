"""
Mr. Dengklek bought N red apples and N green apples. Each red apple weighs A grams and each green apples weighs B grams, and Mr. Dengklek wants to eat some of the apples. However, Mr. Dengklek wants to take as little as possible so that the total weight of the red and green apples has to be the same, and Mr. Dengklek needs to take at least one of each apple. Help Mr. Dengklek calculate the minimum amount of apples he can eat.

e.g.
n = 5, a = 2, b = 3

red apples = 2 * 5 = 10 g
green apples = 3 * 5 = 15 g

Mr. Dengklek eats 2 red apples, so the remaining weight of the red apples is 10 - (2 * 2) = 6 g
Mr. Dengklek eats 3 green apples, so the remaining weight of the green apples is 15 - (3 * 3) = 6 g

Therefore, Mr. Dengklek needs to eat 5 apples so the red apples and the green apples weigh the same

"""

n = int(input("Amount of each apples : "))
a = int(input("Weight of red apples : "))
b = int(input("Weight of green apples : "))

red = n * a
green  = n * b

red -= a #eat one red apple
green -= b #eat one green apple
apples_eaten = 2

while(red != green and red > 0 and green > 0):
    if red > green:
        red -= a
    else:
        green -=b
    apples_eaten += 1

print(f"Mr. Dengklek needs to eat {apples_eaten} apples.")

#complexity = O(n)
