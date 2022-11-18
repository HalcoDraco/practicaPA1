from numba import njit
import sys
from time import time

@njit
def fibo2(n):
    if n < 3:
        return 1
    else:
        return fibo2(n-2) + fibo2(n-1)

num = 100


def fibo(arr, n):
    if len(arr) == 35:
        return arr
    else:
        arr.append(fibo2(n))
        return fibo(arr, n+1)
start = time()
print(fibo([-1], 1))
print(time()-start)