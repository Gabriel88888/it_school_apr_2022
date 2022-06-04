#global scope

PI = 3.14

def correct_pi():
    global PI
    PI = 3.1415412

def p_cerc(r):
    #local scope
    return 2 * PI * r

correct_pi()
print(p_cerc(10))
