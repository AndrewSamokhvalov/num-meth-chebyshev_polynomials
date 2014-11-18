__author__ = 'andrey'

from math import *
import operator
from matplotlib import pyplot as plt


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def ch_polynomial(x, n):
    l_v = []

    for i in range(0, n):
        if i == 0:
            val = 1
        elif i == 1:
            val = x
        else:
            val = 2 * x * l_v[-1] - l_v[-2]

        l_v.append(val)

    return l_v


def ch_root(a, b, N):
    l_k = range(0, N)
    l_t = [cos((k + 1 / 2) * pi / N) for k in l_k]

    #rerange [-1;1] -> [a,b]
    # l_x = [(a + b) / 2 + (b - a) / 2 * t for t in l_t]

    return l_t


def ch_an(n, N, l_root, a, b, function):
    l_k = range(0, N)

    if n == 0:
        c = 1 / N
        l_f = [function(x) for x in l_root]
        ret = c * sum(l_f)

    else:
        c = 2 / N
        l_f = [function(x) for x in l_root]
        l_ch = [cos(((k + 1 / 2) * n * pi) / N) for k in l_k]
        ret = c * sum(list(map(operator.mul, l_ch, l_f)))
    # l_x = [(a + b) / 2 + (b - a) / 2 * t for t in l_ch]

    return ret


def ch_function(l_a, x):
    n = len(l_a)
    l_p = ch_polynomial(x, n)
    buf = list(map(lambda ai, p: ai * p, l_a, l_p))

    return sum(buf)


def example_one():
    a = -1
    b = 1
    d = 0.01
    N = 23

    # function = lambda x: x ** 3 - x ** 2 + x + 10
    function = lambda x: 1 / (1 + 25 * (x ** 2))

    l_x = [x for x in drange(a, b, d)]
    l_f = [function(x) for x in l_x]

    plt.ion()
    for n in range(5, N):
        l_r = ch_root(a, b, n)
        l_a = [ch_an(k, n, l_r, a, b, function) for k in range(0, n)]

        l_ch = [ch_function(l_a, x) for x in l_x]
        l_err = list(map(lambda ch, f: abs(ch - f), l_ch, l_f))

        plt.subplot(2, 1, 1)
        plt.grid(True)
        plt.axis([-1, 1, 0, 1])
        plt.ylabel("Y(x)")
        plt.xlabel("X")
        plt.title('Chebyshev polynomials interpolation N=%i' % n)

        plt.plot(l_x, l_f)
        plt.plot(l_x, l_ch)

        plt.subplot(2, 1, 2)
        plt.grid(True)
        plt.axis([-1, 1, 0, 1])
        plt.ylabel("E(x)")
        plt.xlabel("X")

        plt.plot(l_x, l_err)

        plt.pause(0.5)
        plt.clf()


def example_two():
    pass


def interpolate():
    example_one()


interpolate()









