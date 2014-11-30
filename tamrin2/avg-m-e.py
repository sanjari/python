__author__ = ''

import math
def avg(a):
    x = len(a)
    sum = 0
    for s in a:
        sum = sum + s
    return sum / x
def miana(a):
    a.sort()
    s = len(a)
    if (s % 2) == 0:
        m = a[s/2 -1]
        m2 = a[s/2]
        m3 = m + m2
        return m3/2
    else:
        return a[s/2]

def enheraf(a):
    m = avg(a)
    f = len(a)
    sum1 = 0
    for s in a:
        sum1 = (sum1 + ((s - m) * (s - m)))/(f - 1)
    d = math.sqrt(sum1)
    return d

if __name__ == '__main__':
    a = [10,20,50,40,30]
    print avg(a)
    print miana(a)
    print enheraf(a)
