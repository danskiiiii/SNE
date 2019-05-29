# Wilczewski Daniel
# Cw 10
# python3

from random import randint

def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)

def _log(N):
        a = randint(1, N-1)
        if gcd(N,a) > 1:
            return gcd(N,a)
        else:
            r = 2
            while gcd(N, a ** int(r/2) + 1) == 1 and gcd(N, a ** int(r/2) - 1) == 1:
                r += 1
            if gcd(N, a ** int(r/2) + 1) != 1:
                return gcd(N, a ** int(r/2) + 1)
            else:
                return gcd(N, a ** int(r/2) - 1)

numbers = [12, 91, 143, 1859, 1737, 13843, 988027]
for n in numbers:
    print('n =', n, ':', _log(n))
