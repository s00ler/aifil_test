import sys


def split_vector(N: int, M: int):
    if N <= M or M < 1 or N < 1:
        print('Incorrect parameters')
        return None
    part_size = N // M
    left_shift = N % M
    right_shift = 0
    if left_shift - right_shift > 1:
        left_shift >>= 1
        right_shift = left_shift + (left_shift % 2)
    for i in range(left_shift, N - right_shift, part_size):
        print('[{}, {}]'.format(i, i + part_size - 1))


if __name__ == '__main__':
    try:
        split_vector(int(sys.argv[1]), int(sys.argv[2]))
    except Exception as e:
        print('Invalid usage.',
              'Right way: python task1.py < int number > < int number >')
        print(e)
