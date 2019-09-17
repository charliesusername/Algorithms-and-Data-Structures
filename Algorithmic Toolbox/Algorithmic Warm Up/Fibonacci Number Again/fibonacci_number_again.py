# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    f = [0, 1]
    modF = [0, 1]
    for i in range(2, n + 1):
        f.append(f[-1] + f[-2])
        modF.append(f[-1] % m)
        if ([0, 1] == [modF[-2], modF[-1]]):
            period = modF[0:-2]
            return modF[n % len(period)]
    return modF[-1]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
