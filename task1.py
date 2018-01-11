import sys


def factor(value):
    res = []
    d = 2
    while d * d <= value:
        if value % d == 0:
            res.append(d)
            value //= d
        else:
            d += 1
    if value > 1:
        res.append(value)
    return res


def factorize_vector(N):
    for value in range(1, N + 1):
        print('{}: {}'.format(value, factor(value)))


if __name__ == '__main__':
    try:
        factorize_vector(int(sys.argv[1]))
    except Exception as e:
        print("Invalid usage. Right way: python task1.py < int number >")
        print(e)
