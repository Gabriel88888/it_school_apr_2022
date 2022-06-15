# debug decorator

from datetime import  time


def cube_volume(edge):
    """Calculate cube volume in liters"""

    return edge ** 3 * 1000

l = 29


print("S-a apelat functia cube_volume la ora" , time.now(), "pentru edge=", l)
start = time.time()
cube_volume(l)
stop = time.time()
print("Apelul a durat x sec", stop - start)