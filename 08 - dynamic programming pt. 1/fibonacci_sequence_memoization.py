"""
fibonacci sequence with dynamic programming algorithm

code is from my module
"""
#recursion
def fibonacci(fibo1,n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:
        fibo1 = fibonacci(fibo1,n-1)
        fibo1.append(fibo1[n-3] + fibo1[n-2])
        return fibo1

fibo1 = fibonacci([],11)

print("Fibonacci Sequence using memoization with recursion    :",fibo1)

#linear
fibo2 = [1,1]
for i in range(1,10):
    fibo2.append(fibo2[i] + fibo2[i-1])

print("Fibonacci Sequence using memoization without recursion :",fibo2)
