# Wilczewski Daniel
# Cw 7
# python3

from random import randint

x_s = [ 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0, 0.0]

def _c():
    matrix = [[0 for x in range(25)] for y in range(25)]
    for i in range(25):
        for j in range(25):
            if (i == j):
                matrix[i][j] = 0
            else:
                matrix[i][j] = (x_s[i] - 0.5) *  (x_s[j] - 0.5)
    return matrix

def _w():
    matrix = [[0 for x in range(25)] for y in range(25)]
    c = _c()
    for i in range(25):
        for j in range(25):
            matrix[i][j] = 2 * c[i][j]
    return matrix

def _theta():
    theta = []
    c = _c()
    for i in range(25):
        theta.append(sum(c[i]))
    return theta

def _u(x):
    theta = _theta()
    w = _w()
    u = []
    for i in range(25):
        u.append(sum(k*l for k,l in zip(w[i],x)) - theta[i])
    return u

def _x_0():
    x = []
    for i in range(25):
        x.append(randint(0,1))
    return x

def _x(t, x):
    u = _u(x)
    x_ = []
    for i in range(25):
        if (u[i] > 0):
            x_.append(1)
        elif (u[i] == 0):
            return _x(t-1, x)
        else:
            x_.append(0)
    return x_

def _output(vec):
    image = []
    for element in vec:
        if (element):
            image.append('*')
        else:
            image.append('-')
    return image

def print_matrix( matrix):
    for i in range(1,len(matrix)+1):
        if i % 5 == 0:
            print (matrix[i-1])
        else:
            print(matrix[i-1] ,end =' ')

x0 = _x_0()
x = [x0]

for t in range(1,4):
    x_t = _x(t, x[t-1])
    x.append(x_t)

for element in x:
    print_matrix(_output(element))
    print ()
