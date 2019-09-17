# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    product = 0
    max_first = -1
    max_second = -1
    idx_first = 0
    for i in range(len(numbers)):
        if numbers[i] > max_first:
            max_first = numbers[i]
            idx_first = i
    for j in range(len(numbers)):
        if (numbers[j] > max_second) & (j != idx_first):
            max_second = numbers[j]
    product = max_first * max_second
    return product


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
