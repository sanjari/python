__author__ = ''

def atof(m):
    if m==10:
        s = 'a'
    elif m== 11:
        s = 'b'
    elif m== 12:
        s = 'c'
    elif m== 13:
        s = 'd'
    elif m== 14:
        s = 'e'
    elif m== 15:
        s = 'f'
    else:
        s = m
    return s
def mabna(n):
    x = []
    while (n !=0):
        m = n%16
        if m < 10:
            x.append(m)
        else:
            x.append(atof(m))
        n = n/16
    x.reverse()
    sum1 = ""
    for k in x:
        sum1 = sum1 + str(k)
    return sum1


if __name__ == '__main__':
    print mabna(150)
    print mabna(16)
    print mabna(120)
    print mabna(130)
    print mabna(200)