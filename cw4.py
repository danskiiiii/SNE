# Wilczewski Daniel
# Cw 4
# python3

from random import uniform

EPS = 0.000001
c = 0.01

def first_der(i, x, y, z):
    if i == 0:
        return 4 * x - 2 * y - 2
    elif i == 1:
        return 4 * y - 2 * x - 2 * z
    else:
        return 2 * z - 2 * y

def sec_der(i, x, y):
    if i == 0:
        return 12 * x**3 + 12 * x**2 - 24 * x
    else:
        return 24 * y - 24

def first_min(old_x):
    new_x = [0, 0, 0]
    for i in range(len(new_x)):
        new_x[i] = old_x[i] - c * first_der(i, old_x[0], old_x[1], old_x[2])
    while max(abs(x - y) for x, y in zip(new_x, old_x)) > EPS:
        old_x = list(new_x)
        for i in range(len(new_x)):
            new_x[i] = old_x[i] - c * first_der(i, old_x[0], old_x[1], old_x[2])
    return new_x

def sec_min(old_x):
    new_x = [0, 0]
    for i in range(len(new_x)):
        new_x[i] = old_x[i] - c * sec_der(i, old_x[0], old_x[1])
    while max(abs(x - y) for x, y in zip(new_x, old_x)) > EPS:
        old_x = list(new_x)
        for i in range(len(new_x)):
            new_x[i] = old_x[i] - c * sec_der(i, old_x[0], old_x[1])
    return new_x

def calc_f(x, y, z):
    return 2 * x**2 + 2 * y**2 + z**2 - 2 * x * y - 2 * y * z - 2 * x + 3

def calc_g(x, y):
    return 3 * x**4 + 4 * x**3 - 12 * x**2 + 12 * y**2 - 24 * y

v_3 = [ uniform(1,4) for x in range(3) ]
print(f'\nmin f:\nv = {first_min(v_3)}')
print(f'f(v) = {calc_f(first_min(v_3)[0], first_min(v_3)[1], first_min(v_3)[2])}')

# v_2 = [ uniform(1,4) for x in range(2) ]
v_2 = [4,4] # ==> (-2,1)        # v_2 = [2,1] ==> (1,1)
print(f'\nmin g:\nv = {sec_min(v_2)}')
print(f'g(v) = {calc_g(sec_min(v_2)[0],sec_min(v_2)[1])}')