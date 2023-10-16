import random


def binary(number_k):
    k = []
    while number_k > 0:
        r = int(number_k % 2)
        k.append(r)
        number_k = number_k // 2
    k.reverse()
    return k


def square_integer(number_a, number_k, number_n):
    k = binary(number_k)
    k.reverse()
    a = number_a
    if k[0] == 1:
        b = number_a
    else:
        b = 1
    for i in range(1, len(k)):
        a = (a * a) % number_n
        if k[i] == 1:
            b = (b * a) % number_n
    return b


def fermat(n,t):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    for _ in range(t):
        a = random.randint(2, n - 2)
        r = square_integer(a, n - 1, n)
        if r != 1:
            return False
    return True


if __name__ == '__main__':
    n = int(input('Nhập n = '))
    t = int(input('Nhập t = '))
    if fermat(n,t) and n % 2 != 0 or n == 2:
        print('Số nguyên tố')
    else:
        print('Hợp số')
