# Wilczewski Daniel
# Cw 5
# python3

from math import exp
from random import uniform

def f(u):
    return 1.0 / (1.0 + exp(-1 * beta * u))

def Df(u):
    return beta * f(u) * (1.0 - f(u))

def calc_x(w):
    x = []
    for i in range(len(u)):
        x1 = f(sum(k*l for k, l in zip(w[0], u[i])))
        x2 = f(sum(k*l for k, l in zip(w[1], u[i])))
        x.append([x1, x2, 1])
    return x

def calc_y(x, s):
    y = []
    for i in range(len(x)):
        yp = f(sum(k*l for k,l in zip(s, x[i])))
        y.append(yp)
    return y

def DE_s(x, y, s):
    derivative = []
    for i in range(3):
        temp = 0
        for p in range(4):
            temp += (y[p] - z[p]) * Df(sum(k*l for k,l in zip(s, x[p]))) * x[p][i]
        derivative.append(temp)
    return derivative

def DE_w(x, y, s, w):
    derivative = []
    for i in range(2):
        row = []
        for j in range(3):
            temp = 0
            for p in range(4):
                temp += (y[p] - z[p]) * Df(sum(k*l for k, l in zip(s, x[p]))) * s[i] * Df(sum(k*l for k, l in zip(w[i], u[p]))) * u[p][j]
            row.append(temp)
        derivative.append(row)
    return derivative


def calc_new_s(old, derivative):
    s = []
    for i in range(3):
        temp = old[i] - c * derivative[i]
        s.append(temp)
    return s

def calc_new_w(old, derivative):
    w = []
    for i in range(2):
        row = []
        for j in range(3):
            temp = old[i][j] - c * derivative[i][j]
            row.append(temp)
        w.append(row)
    return w

c = 0.1
beta = round(uniform(1.0,3.0), 3)
epsilon = 0.00001
u = [[0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
z = [0, 1, 1, 0]
old_s, old_w = [0,1,2], [[0,1,2],[0,1,2]]

x = calc_x(old_w)
y = calc_y(x, old_s)
der_s = DE_s(x, y, old_s)
der_w = DE_w(x, y, old_s, old_w)
new_s = calc_new_s(old_s, der_s)
new_w = calc_new_w(old_w, der_w)
iteration = 1

while max(max(abs( n-o) for n,o in zip(new_s, old_s)),
          max(abs(n-o) for n,o in zip(new_w[0], old_w[0])),
          max(abs(n-o) for n,o in zip(new_w[1], old_w[1]))) > epsilon:

    old_s, old_w = new_s, new_w
    iteration += 1
    x = calc_x(old_w)
    y = calc_y(x, old_s)
    der_s = DE_s(x, y, old_s)
    der_w = DE_w(x, y, old_s, old_w)
    new_s = calc_new_s(old_s, der_s)
    new_w = calc_new_w(old_w, der_w)

print(f"\nbeta: {beta}, c: {c}, epsilon: {epsilon}")
print(f"iteracja: {iteration}")
print("\nZadanie 1:")
print(f"w = {[ round(x,2) for x in new_w[0] ], [ round(x,2) for x in new_w[1] ]}")
print(f"s = {[ round(x,2) for x in new_s ]}")
print(f"\nZadanie 2:\ny = {[ round(x,2) for x in y ]}")