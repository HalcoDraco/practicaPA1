cpdef int hola():
    cdef int a = 0
    cdef int i = 0
    for i in range(10**8):
        a += 1
    return a

from time import time

t = time()
print(hola())
print(time() - t)