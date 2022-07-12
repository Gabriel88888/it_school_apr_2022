# 1 Write a script that calculates first 1000 numbers from Fibonacci sequence and 
# print how much execution took.

import time
from datetime import datetime



def fib(n):

    a = 0
    b = 1

    if n == 1:
        print(a)

    for i in range(2, n):

        c = a + b
        a = b
        b = c
        print(c)

fib(100)

script_start_time = datetime.now()
for i in range(10000):
    j = 10 + 1

# end_time = time.time()
# final_time = end_time - start_time
# print(final_time)

script_end_time = datetime.now()
print(script_end_time - script_start_time)