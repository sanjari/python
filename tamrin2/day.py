__author__ = 'GOD'

__author__ = ''

def day(n):
    if n > 366:
        return "overflu"
    else:
        if n <= 186:
            m = n/31
            d = n % 31
            return m ,d
        elif 187<n<337:
            m=n/30
            d=(n-186)%30
            return m+1,d
        elif 336<n<366:
            m=(n-337)/29
            d=(n-336)
            return m+12,d
        else:
            return

if __name__ == '__main__':
    print day(368)
    print(day(90))
    print(day(337))
    print(day(156))

